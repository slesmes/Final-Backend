from typing import List
from src.schemas.sale import Sale
from src.models.sale import Sale as saleModel

class saleRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_sales(self) -> List[Sale]:
        query = self.db.query(saleModel)
        return query.all()

    def get_sale(self, id: int ) -> Sale:
        element = self.db.query(saleModel).filter(saleModel.id == id).first()
        return element
    
    def create_sale(self, sale: Sale) -> dict:
        new_sale = saleModel(**sale.model_dump())
        self.db.add(new_sale)
        self.db.commit()
        self.db.refresh(new_sale)
        return new_sale
    
    def delete_sale(self, id: int) -> dict:
        element: Sale = self.db.query(saleModel).filter(saleModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  