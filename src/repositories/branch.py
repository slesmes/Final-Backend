from typing import List

from fastapi import HTTPException
from src.schemas.branch import Branch
from src.models.branch import Branch as branchModel


class branchRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_branchs(self) -> List[Branch]:
        query = self.db.query(branchModel)
        return query.all()

    def get_branch(self, id: int ) -> Branch:
        element = self.db.query(branchModel).filter(branchModel.id == id).first()
        return element
    
    def update_branch(self, id:int, branch:Branch)-> dict:
        Updatebranch: Branch= self.db.query(branchModel).filter(branchModel.id == id, branchModel.id_company == branch.id_company).first()  
        if Updatebranch is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        Updatebranch.name = branch.name
        Updatebranch.id_city = branch.id_city
        Updatebranch.id_company = branch.id_company   
        Updatebranch.address = branch.address
        Updatebranch.status = branch.status
        Updatebranch.phone = branch.phone

        self.db.commit()
        self.db.refresh(Updatebranch)
        return Updatebranch
    
    def create_branch(self, branch: Branch) -> dict:
        new_branch = branchModel(**branch.model_dump())
        self.db.add(new_branch)
        self.db.commit()
        self.db.refresh(new_branch)
        return new_branch
    
    def delete_branch(self, id: int) -> dict:
        element: Branch = self.db.query(branchModel).filter(branchModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  
    