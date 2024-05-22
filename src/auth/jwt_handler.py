import bcrypt
import jwt
from fastapi import Depends, HTTPException
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from src.repositories.user import UserRepository
from src.models.user import User
from src.config.database import SessionLocal
import json

class JWTHandler:
    def __init__(self, secret, algorithm) -> None:
        self.secret = secret
        self.algorithm = algorithm

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password=password.encode("utf-8"),salt=bcrypt.gensalt())
    
    def verify_password(self,
        password: str,
        hashed_password: str) -> bool:
        return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=hashed_password.encode("utf-8"),)
    
    def encode_token(self, user):
        from src.routers.branch import get_branch_by_id
        id_branch = user.id_branch
        branch = get_branch_by_id(id_branch)
        json_string = branch.body.decode('utf-8')
        company = json.loads(json_string)["id_company"]
        payload = {
            # exp (expiration time): Time after which the JWT expires
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=1),
            # iat (issued at time): Time at which the JWT was issued
            "iat": datetime.now(tz=timezone.utc),
            # sub (subject): Subject of the JWT (the user)
            "sub": user.username,
            # Custom Issues
            "scope": "access_token",
            "user.branch": user.id_branch,
            "user.rol": user.id_rol,
            "user.email": user.email,
            "user.id": user.identification,
            "user.company": company
        }
        print(payload)
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)
    
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            if payload["scope"] == "access_token":
                return payload
            raise HTTPException(status_code=401, detail="Scope for the token is invalid")
        except jwt.ExpiredSignatureError: raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError: raise HTTPException(status_code=401, detail="Invalid token")
    
    def encode_refresh_token(self, user):
        payload = {
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=10),
            "iat": datetime.now(tz=timezone.utc),
            "scope": "refresh_token",
            "sub": user.email,
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)
    
    def refresh_token(self, refresh_token):
            try:
                payload = jwt.decode(refresh_token, self.secret, algorithms=[self.algorithm])
                if payload and payload["scope"] == "refresh_token":
                    user = UserRepository.get_user(payload["sub"])
                    new_token = self.encode_token(user)
                    return new_token
                raise HTTPException(status_code=401, detail="Invalid scope for token")
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Refresh token expired")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="Invalid refresh token")
            
    def get_current_user(self, token) -> User:
        db = SessionLocal()
        payload = self.decode_token(token)
        user_id = payload.get("user.id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = UserRepository(db).get_User(int(user_id))
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user.id