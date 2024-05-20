from typing import List

from fastapi import HTTPException
from src.schemas.product import Product
from src.models.product import Product as productModel

class productRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_products(self) -> List[Product]:
        query = self.db.query(productModel)
        return query.all()

    def get_product(self, id: int ) -> Product:
        element = self.db.query(productModel).filter(productModel.id == id).first()
        return element
    
    def create_product(self, product: Product) -> dict:
        new_product = productModel(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product
    
    def update_product(self, id:str,product:Product)-> dict:
        Updateproduct: Product= self.db.query(productModel).filter(productModel.id == id, productModel.id_branch == product.id_branch, productModel.id_category == product.id_category).first()  
        if Updateproduct is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updateproduct.name = product.name
        Updateproduct.id_branch = product.id_branch
        Updateproduct.price = product.price
        Updateproduct.quantity = product.quantity
        Updateproduct.description = product.description
        Updateproduct.disccount = product.disccount
        Updateproduct.id_category = product.id_category
        Updateproduct.status = product.status


        self.db.commit()
        self.db.refresh(Updateproduct)
        return Updateproduct

    def delete_product(self, id: int) -> dict:
        element: Product = self.db.query(productModel).filter(productModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element 