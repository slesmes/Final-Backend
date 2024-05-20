from typing import List
from src.schemas.bill import Bill
from src.models.bill import Bill as billModel

class billRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_bills(self) -> List[Bill]:
        query = self.db.query(billModel)
        return query.all()

    def get_bill(self, id: int ) -> Bill:
        element = self.db.query(billModel).filter(billModel.id == id).first()
        return element
    
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
    
    def update_bill(self, id: int, bill_data: Bill) -> dict:
        bill = self.db.query(billModel).filter(billModel.id == id).first()        
        bill.date_bill= bill_data.date_bill
        bill.status= bill_data.status
        self.db.commit()
        self.db.refresh(bill)
        return bill  
    