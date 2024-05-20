from typing import List

from fastapi import HTTPException
from src.schemas.company import Company
from src.models.company import Company as companyModel

class companyRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_companies(self) -> List[Company]:
        query = self.db.query(companyModel)
        return query.all()

    def get_company(self, id: int ) -> Company:
        element = self.db.query(companyModel).filter(companyModel.id == id).first()
        return element
    
    def create_company(self, company: Company) -> dict:
        new_company = companyModel(**company.model_dump())
        self.db.add(new_company)
        self.db.commit()
        self.db.refresh(new_company)
        return new_company
    
    def update_company(self, nit:str, company:Company)-> dict:
        Updatecompany: Company= self.db.query(companyModel).filter(companyModel.nit == nit, companyModel.id_city == company.id_city).first()  
        if Updatecompany is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatecompany.name = company.name
        Updatecompany.address = company.address   
        Updatecompany.id_city = company.id_city  
        Updatecompany.phone = company.phone
        Updatecompany.status = company.status  

        self.db.commit()
        self.db.refresh(Updatecompany)
        return Updatecompany
    
    def delete_company(self, id: int) -> dict:
        element: Company = self.db.query(companyModel).filter(companyModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  