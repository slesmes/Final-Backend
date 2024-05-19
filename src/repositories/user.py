from typing import List
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
    
    def get_user(self, email: str) -> User:
        element = self.db.query(UserModel).filter(UserModel.email == email).first()
        return element
    
    def create_User(self, user: User) -> dict:
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def remove_user(self, id: int ) -> dict:
        element: User = self.db.query(UserModel).filter(UserModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element    