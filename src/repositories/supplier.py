from typing import List

from fastapi import HTTPException
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
    
    def update_supplier(self, id:str,supplier:Supplier)-> dict:
        Updatesupplier: Supplier= self.db.query(supplierModel).filter(supplierModel.id == id).first()  
        if Updatesupplier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatesupplier.name = supplier.name
        Updatesupplier.name_seller = supplier.name_seller
        Updatesupplier.phone = supplier.phone
        Updatesupplier.status = supplier.status



        self.db.commit()
        self.db.refresh(Updatesupplier)
        return Updatesupplier

    def delete_supplier(self, id: int) -> dict:
        element: Supplier = self.db.query(supplierModel).filter(supplierModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  