from typing import List

from fastapi import HTTPException
from src.schemas.productXsupplier import ProductXsupplier
from src.models.productXsupplier import Productxsupplier as productXsupplierModel

class productXsupplierRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_productXsuppliers(self, branch:int) -> List[ProductXsupplier]:
        query = self.db.query(productXsupplierModel).filter(productXsupplierModel.id_branch == branch)
        return query.all()

    def get_productXsupplier(self, id: int, branch:int ) -> ProductXsupplier:
        element = self.db.query(productXsupplierModel).filter(productXsupplierModel.id == id, productXsupplierModel.id_branch == branch).first()
        return element
    
    def create_productXsupplier(self, productXsupplier: ProductXsupplier) -> dict:
        new_productXsupplier = productXsupplierModel(**productXsupplier.model_dump())
        self.db.add(new_productXsupplier)
        self.db.commit()
        self.db.refresh(new_productXsupplier)
        return new_productXsupplier
    
    def update_productXsupplier(self, id:str,productXsupplier:ProductXsupplier)-> dict:
        Updateproductxsupplier: ProductXsupplier= self.db.query(productXsupplierModel).filter(productXsupplierModel.id == id).first()  
        if Updateproductxsupplier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updateproductxsupplier.id_branch = productXsupplier.id_branch
        Updateproductxsupplier.id_product = productXsupplier.id_product
        Updateproductxsupplier.id_supplier = productXsupplier.id_supplier


        self.db.commit()
        self.db.refresh(Updateproductxsupplier)
        return Updateproductxsupplier

    def delete_productXsupplier(self, id: int, branch:int) -> dict:
        element: ProductXsupplier = self.db.query(productXsupplierModel).filter(productXsupplierModel.id == id, productXsupplierModel.id_branch == branch).first()
        self.db.delete(element)
        self.db.commit()
        return element  