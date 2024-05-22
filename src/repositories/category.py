from typing import List

from fastapi import HTTPException
from src.schemas.category import Category
from src.models.category import Category as categoryModel

class categoryRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_categorys(self) -> List[Category]:
        query = self.db.query(categoryModel)
        return query.all()

    def get_category(self, id: int ) -> Category:
        element = self.db.query(categoryModel).filter(categoryModel.id == id).first()
        return element
    
    def create_category(self, category: Category) -> dict:
        new_category = categoryModel(**category.model_dump())
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category
    
    def update_branch(self, id:int, category:Category)-> dict:
        Updatecategory: Category= self.db.query(categoryModel).filter(categoryModel.id == id, categoryModel.id_branch == category.id_branch).first()  
        if Updatecategory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatecategory.name = category.name
        Updatecategory.description = category.description
        Updatecategory.id_branch = category.id_branch   
        Updatecategory.status = category.status

        self.db.commit()
        self.db.refresh(Updatecategory)
        return Updatecategory
    
    def delete_category(self, id: int) -> dict:
        element: Category = self.db.query(categoryModel).filter(categoryModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  
    