from typing import List
from src.schemas.supplierXbranch import SupplierXBranch
from src.models.supplierXbranch import Supplierxbranch as supplierXbranchModel

class supplierXbranchRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_supplierXbranchs(self) -> List[SupplierXBranch]:
        query = self.db.query(supplierXbranchModel)
        return query.all()

    def get_supplierXbranch(self, id: int ) -> SupplierXBranch:
        element = self.db.query(supplierXbranchModel).filter(supplierXbranchModel.id == id).first()
        return element
    
    def create_supplierXbranch(self, supplierXbranch: SupplierXBranch) -> dict:
        new_supplierXbranch = supplierXbranchModel(**supplierXbranch.model_dump())
        self.db.add(new_supplierXbranch)
        self.db.commit()
        self.db.refresh(new_supplierXbranch)
        return new_supplierXbranch
    
    def delete_supplierXbranch(self, id: int) -> dict:
        element: SupplierXBranch = self.db.query(supplierXbranchModel).filter(supplierXbranchModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  