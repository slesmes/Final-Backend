from typing import List
from src.schemas.supplier import Supplier
from src.models.supplier import Supplier as supplierModel

class supplierRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_suppliers(self) -> List[Supplier]:
        query = self.db.query(supplierModel)
        return query.all()

    def get_supplier(self, id: int ) -> Supplier:
        element = self.db.query(supplierModel).filter(supplierModel.id == id).first()
        return element
    
    def create_supplier(self, supplier: Supplier) -> dict:
        new_supplier = supplierModel(**supplier.model_dump())
        self.db.add(new_supplier)
        self.db.commit()
        self.db.refresh(new_supplier)
        return new_supplier
    
    def delete_supplier(self, id: int) -> dict:
        element: Supplier = self.db.query(supplierModel).filter(supplierModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  