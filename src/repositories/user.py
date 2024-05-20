from typing import List

from fastapi import HTTPException
from src.schemas.user import User
from src.models.user import User as UserModel


class UserRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_Users(self) -> List[User]:
        query = self.db.query(UserModel)
        return query.all()
    
    def get_User(self, id: int) -> User:
        element = self.db.query(UserModel).filter(UserModel.id == id).first()
        return element
    
    def get_user(self, username: str) -> User:
        element = self.db.query(UserModel).filter(UserModel.username == username).first()
        return element
    
    def create_User(self, user: User) -> dict:
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, id:str, user:User)-> dict:
        Updateuser: User= self.db.query(UserModel).filter(UserModel.identification == id, UserModel.id_branch == user.id_branch).first()  
        if Updateuser is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updateuser.name = user.name
        Updateuser.lastname = user.lastname  
        Updateuser.email = user.email  
        Updateuser.id_branch = user.id_branch  
        Updateuser.id_rol = user.id_rol  
        Updateuser.phone = user.phone
        Updateuser.status = user.status  

        self.db.commit()
        self.db.refresh(Updateuser)
        return Updateuser

    def remove_user(self, id: int ) -> dict:
        element: User = self.db.query(UserModel).filter(UserModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element    