from typing import List
from src.schemas.supplierXpart import SupplierXpart
from src.models.supplierXpart import Supplierxpart as supplierXpartModel


class supplierXpartRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_supplierXparts(self) -> List[SupplierXpart]:
        query = self.db.query(supplierXpartModel)
        return query.all()
    
    def get_supplierXpart(self, id: int) -> SupplierXpart:
        element = self.db.query(supplierXpartModel).filter(supplierXpartModel.id == id).first()
        return element
    
    def get_supplierXpart(self, email: str) -> SupplierXpart:
        element = self.db.query(supplierXpartModel).filter(supplierXpartModel.email == email).first()
        return element
    
    def create_supplierXpart(self, supplierXpart: SupplierXpart) -> dict:
        new_supplierXpart = supplierXpartModel(**supplierXpart.model_dump())
        self.db.add(new_supplierXpart)
        self.db.commit()
        self.db.refresh(new_supplierXpart)
        return new_supplierXpart
    
    def remove_supplierXpart(self, id: int ) -> dict:
        element: SupplierXpart = self.db.query(supplierXpartModel).filter(supplierXpartModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element   