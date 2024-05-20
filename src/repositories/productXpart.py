from typing import List
from src.schemas.productXpart import ProductXpart
from src.models.productXpart import Productxpart as productXpartModel

class productXpartRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_productXparts(self) -> List[ProductXpart]:
        query = self.db.query(productXpartModel)
        return query.all()

    def get_productXpart(self, id: int ) -> ProductXpart:
        element = self.db.query(productXpartModel).filter(productXpartModel.id == id).first()
        return element
    
    def create_productXpart(self, productXpart: ProductXpart) -> dict:
        new_productXpart = productXpartModel(**productXpart.model_dump())
        self.db.add(new_productXpart)
        self.db.commit()
        self.db.refresh(new_productXpart)
        return new_productXpart
    
    def delete_productXpart(self, id: int) -> dict:
        element: ProductXpart = self.db.query(productXpartModel).filter(productXpartModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  