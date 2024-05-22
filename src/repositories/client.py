from typing import List

from fastapi import HTTPException
from src.schemas.client import Client
from src.models.client import Client as clientModel

class clientRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_clients(self, company:str) -> List[Client]:
        query = self.db.query(clientModel).filter(clientModel.id_company == company)
        return query.all()

    def get_client(self, id: int, company:str ) -> Client:
        element = self.db.query(clientModel).filter(clientModel.id == id, clientModel.id_company == company).first()
        return element
    
    def create_client(self, client: Client) -> dict:
        new_client = clientModel(**client.model_dump())
        self.db.add(new_client)
        self.db.commit()
        self.db.refresh(new_client)
        return new_client
    
    def update_client(self, id:str, client:Client)-> dict:
        Updateclient: Client= self.db.query(clientModel).filter(clientModel.identification == id).first()  
        if Updateclient is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updateclient.name = client.name
        Updateclient.address = client.address  
        Updateclient.lastname = client.lastname  
        Updateclient.email = client.email  
        Updateclient.id_city = client.id_city  
        Updateclient.id_company = client.id_company  
        Updateclient.phone = client.phone
        Updateclient.status = client.status  

        self.db.commit()
        self.db.refresh(Updateclient)
        return Updateclient
    
    def delete_client(self, id: int, company:str) -> dict:
        element: Client = self.db.query(clientModel).filter(clientModel.id == id, clientModel.id_company  == company).first()
        self.db.delete(element)
        self.db.commit()
        return element  