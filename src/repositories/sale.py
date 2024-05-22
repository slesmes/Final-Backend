from typing import List

from fastapi import HTTPException
from src.schemas.sale import Sale
from src.models.sale import Sale as saleModel

class saleRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_sales(self, branch:int) -> List[Sale]:
        query = self.db.query(saleModel).filter(saleModel.id_branch == branch)
        return query.all()

    def get_sale(self, id: int, branch: int ) -> Sale:
        element = self.db.query(saleModel).filter(saleModel.id == id, saleModel.id_branch == branch).first()
        return element
    
    def create_sale(self, sale: Sale) -> dict:
        new_sale = saleModel(**sale.model_dump())
        self.db.add(new_sale)
        self.db.commit()
        self.db.refresh(new_sale)
        return new_sale
    
    def update_sale(self, id:str,sale:Sale)-> dict:
        Updatesale: Sale= self.db.query(saleModel).filter(saleModel.id == id).first()  
        if Updatesale is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatesale.id_branch = sale.id_branch
        Updatesale.id_bill = sale.id_bill
        Updatesale.id_product = sale.id_product
        Updatesale.quantity = sale.quantity


        self.db.commit()
        self.db.refresh(Updatesale)
        return Updatesale

    def delete_sale(self, id: int, branch:int) -> dict:
        element: Sale = self.db.query(saleModel).filter(saleModel.id == id, saleModel.id_branch == branch).first()
        self.db.delete(element)
        self.db.commit()
        return element  