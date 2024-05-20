from typing import List

from fastapi import HTTPException
from src.schemas.country import Country
from src.models.country import Country as CountryModel

class CountryRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_countries(self) -> List[Country]:
        query = self.db.query(CountryModel)
        return query.all()

    def get_country(self, id: int ) -> Country:
        element = self.db.query(CountryModel).filter(CountryModel.id == id).first()
        return element
    
    def create_country(self, country: Country) -> dict:
        new_country = CountryModel(**country.model_dump())
        self.db.add(new_country)
        self.db.commit()
        self.db.refresh(new_country)
        return new_country
    
    def update_country(self, id:str,country:Country)-> dict:
        Updatecountry: Country= self.db.query(CountryModel).filter(CountryModel.id == id).first()  
        if Updatecountry is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatecountry.name = country.name

        self.db.commit()
        self.db.refresh(Updatecountry)
        return Updatecountry
    
    def delete_country(self, id: int) -> dict:
        element: Country = self.db.query(CountryModel).filter(CountryModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  