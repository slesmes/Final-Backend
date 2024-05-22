from typing import List

from fastapi import HTTPException
from src.schemas.city import City
from src.models.city import City as cityModel

class cityRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_cities(self) -> List[City]:
        query = self.db.query(cityModel)
        return query.all()

    def get_city(self, id: int ) -> City:
        element = self.db.query(cityModel).filter(cityModel.id == id).first()
        return element
    
    def create_city(self, city: City) -> dict:
        new_city = cityModel(**city.model_dump())
        self.db.add(new_city)
        self.db.commit()
        self.db.refresh(new_city)
        return new_city
    

    def update_branch(self, id:int, city:City)-> dict:
        Updatecity: City= self.db.query(cityModel).filter(cityModel.id == id, cityModel.id_department == city.id_department).first()  
        if Updatecity is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatecity.name = city.name
        Updatecity.id_department = city.id_department
        Updatecity.postal_code = city.postal_code   

        self.db.commit()
        self.db.refresh(Updatecity)
        return Updatecity
    
    def delete_city(self, id: int) -> dict:
        element: City = self.db.query(cityModel).filter(cityModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  
    