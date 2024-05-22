from typing import List

from fastapi import HTTPException
from src.schemas.part import Part
from src.models.part import Part as partModel

class partRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_parts(self, branch: int) -> List[Part]:
        query = self.db.query(partModel).filter(partModel.id_branch == branch)
        return query.all()

    def get_part(self, id: int, branch:int ) -> Part:
        element = self.db.query(partModel).filter(partModel.id == id, partModel.id_branch == branch).first()
        return element
    
    def create_part(self, part: Part) -> dict:
        new_part = partModel(**part.model_dump())
        self.db.add(new_part)
        self.db.commit()
        self.db.refresh(new_part)
        return new_part
    
    def update_part(self, id:str,part:Part)-> dict:
        Updatepart: Part= self.db.query(partModel).filter(partModel.id == id, partModel.id_branch == part.id_branch).first()  
        if Updatepart is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatepart.name = part.name
        Updatepart.id_branch = part.id_branch
        Updatepart.price = part.price
        Updatepart.quantity = part.quantity


        self.db.commit()
        self.db.refresh(Updatepart)
        return Updatepart
    
    def delete_part(self, id: int, branch:int) -> dict:
        element: Part = self.db.query(partModel).filter(partModel.id == id, partModel.id_branch == branch).first()
        self.db.delete(element)
        self.db.commit()
        return element 