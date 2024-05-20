from typing import List
from src.schemas.part import Part
from src.models.part import Part as partModel

class partRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_parts(self) -> List[Part]:
        query = self.db.query(partModel)
        return query.all()

    def get_part(self, id: int ) -> Part:
        element = self.db.query(partModel).filter(partModel.id == id).first()
        return element
    
    def create_part(self, part: Part) -> dict:
        new_part = partModel(**part.model_dump())
        self.db.add(new_part)
        self.db.commit()
        self.db.refresh(new_part)
        return new_part
    
    def delete_part(self, id: int) -> dict:
        element: Part = self.db.query(partModel).filter(partModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element 