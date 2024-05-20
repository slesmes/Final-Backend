from typing import List
from src.schemas.rol import Rol
from src.models.rol import Rol as rolModel

class rolRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_rols(self) -> List[Rol]:
        query = self.db.query(rolModel)
        return query.all()

    def get_rol(self, id: int ) -> Rol:
        element = self.db.query(rolModel).filter(rolModel.id == id).first()
        return element
    
    def create_rol(self, rol: Rol) -> dict:
        new_rol = rolModel(**rol.model_dump())
        self.db.add(new_rol)
        self.db.commit()
        self.db.refresh(new_rol)
        return new_rol
    
    def delete_rol(self, id: int) -> dict:
        element: Rol = self.db.query(rolModel).filter(rolModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  