from typing import List
from src.schemas.bill import Bill
from src.models.bill import Bill as billModel
from fastapi import HTTPException


class billRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_bills(self) -> List[Bill]:
        query = self.db.query(billModel)
        return query.all()

    def get_bill(self, id: int ) -> Bill:
        element = self.db.query(billModel).filter(billModel.id == id).first()
        return element
    
    def update_bill(self, id:int, bill:Bill)-> dict:
        Updatebill: Bill= self.db.query(billModel).filter(billModel.id == id, billModel.id_user == bill.id_user, billModel.id_client == bill.id_client, billModel.id_branch == bill.id_branch).first()  
        if Updatebill is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatebill.id_branch = bill.id_branch
        Updatebill.id_client = bill.id_client
        Updatebill.id_user = bill.id_user   
        Updatebill.date_bill = bill.date_bill
        Updatebill.status = bill.status

        self.db.commit()
        self.db.refresh(Updatebill)
        return Updatebill

    
    def create_bill(self, bill: Bill) -> dict:
        new_bill = billModel(**bill.model_dump())
        self.db.add(new_bill)
        self.db.commit()
        self.db.refresh(new_bill)
        return new_bill
    
    def delete_bill(self, id: int) -> dict:
        element: Bill = self.db.query(billModel).filter(billModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  