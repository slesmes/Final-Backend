from typing import List

from fastapi import HTTPException
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
    
    def update_supplierXbranch(self, id:str,supplierXbranch:SupplierXBranch)-> dict:
        UpdatesupplierXbranch: SupplierXBranch= self.db.query(supplierXbranchModel).filter(supplierXbranchModel.id == id).first()  
        if UpdatesupplierXbranch is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        UpdatesupplierXbranch.id_branch = supplierXbranch.id_branch
        UpdatesupplierXbranch.id_supplier = supplierXbranch.id_supplier

        self.db.commit()
        self.db.refresh(UpdatesupplierXbranch)
        return UpdatesupplierXbranch


    def delete_supplierXbranch(self, id: int) -> dict:
        element: SupplierXBranch = self.db.query(supplierXbranchModel).filter(supplierXbranchModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  