from fastapi import HTTPException, status
from src.repositories.user import UserRepository
from src.config.database import SessionLocal
from src.auth import auth_handler
from src.schemas.user import LoginUser as UserLoginSchema
from src.schemas.user import User as UserCreateSchema


class AuthRepository:
    def __init__(self) -> None:
        pass


    def register_user(self, user: UserCreateSchema) -> dict:
        db = SessionLocal()
        if UserRepository(db).get_user(username=user.username) != None:
            raise Exception("Account already exists")
        hashed_password = auth_handler.hash_password(password=user.password)
        new_user: UserCreateSchema = UserCreateSchema(
        identification= user.identification,
        name=user.name,
        lastname=user.lastname,
        phone=user.phone,
        id_rol = user.id_rol,
        id_branch = user.id_branch,
        username = user.username,
        email=user.email,
        password=hashed_password,
        status=user.status,

        )
        return UserRepository(db).create_User(new_user)

    def login_user(self, user: UserLoginSchema) -> dict:
        db = SessionLocal()
        check_user = UserRepository(db).get_user(username=user.username)
        if check_user is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials (1)",
            )

        if not check_user.status:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The user is not allowed to log in",
            )
        if not auth_handler.verify_password(user.password, check_user.password):
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials (2)",
            )
        access_token = auth_handler.encode_token(check_user)
        refresh_token = auth_handler.encode_refresh_token(check_user)
        return access_token, refresh_token
