from typing import List

from fastapi import HTTPException
from src.schemas.rol import Rol
from src.models.rol import Rol as rolModel

class rolRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_rols(self, branch: int) -> List[Rol]:
        query = self.db.query(rolModel).filter(rolModel.id_branch == branch)
        return query.all()

    def get_rol(self, id: int, branch:int ) -> Rol:
        element = self.db.query(rolModel).filter(rolModel.id == id, rolModel.id_branch == branch).first()
        return element
    
    def create_rol(self, rol: Rol) -> dict:
        new_rol = rolModel(**rol.model_dump())
        self.db.add(new_rol)
        self.db.commit()
        self.db.refresh(new_rol)
        return new_rol
    
    def update_rol(self, id:str,rol:Rol)-> dict:
        Updaterol: Rol= self.db.query(rolModel).filter(rolModel.id == id).first()  
        if Updaterol is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updaterol.id_branch = rol.id_branch
        Updaterol.name = rol.name
        Updaterol.description = rol.description


        self.db.commit()
        self.db.refresh(Updaterol)
        return Updaterol
    
    def delete_rol(self, id: int, branch: int) -> dict:
        element: Rol = self.db.query(rolModel).filter(rolModel.id == id, rolModel.id_branch == branch).first()
        self.db.delete(element)
        self.db.commit()
        return element  