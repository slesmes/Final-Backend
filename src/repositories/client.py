from typing import List
from src.schemas.client import Client
from src.models.client import Client as clientModel

class clientRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_clients(self) -> List[Client]:
        query = self.db.query(clientModel)
        return query.all()

    def get_client(self, id: int ) -> Client:
        element = self.db.query(clientModel).filter(clientModel.id == id).first()
        return element
    
    def create_client(self, client: Client) -> dict:
        new_client = clientModel(**client.model_dump())
        self.db.add(new_client)
        self.db.commit()
        self.db.refresh(new_client)
        return new_client
    
    def delete_client(self, id: int) -> dict:
        element: Client = self.db.query(clientModel).filter(clientModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  