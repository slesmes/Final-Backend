from typing import List
from src.schemas.productXsupplier import ProductXsupplier
from src.models.productXsupplier import Productxsupplier as productXsupplierModel

class productXsupplierRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_productXsuppliers(self) -> List[ProductXsupplier]:
        query = self.db.query(productXsupplierModel)
        return query.all()

    def get_productXsupplier(self, id: int ) -> ProductXsupplier:
        element = self.db.query(productXsupplierModel).filter(productXsupplierModel.id == id).first()
        return element
    
    def create_productXsupplier(self, productXsupplier: ProductXsupplier) -> dict:
        new_productXsupplier = productXsupplierModel(**productXsupplier.model_dump())
        self.db.add(new_productXsupplier)
        self.db.commit()
        self.db.refresh(new_productXsupplier)
        return new_productXsupplier
    
    def delete_productXsupplier(self, id: int) -> dict:
        element: ProductXsupplier = self.db.query(productXsupplierModel).filter(productXsupplierModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  