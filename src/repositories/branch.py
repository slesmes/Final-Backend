from typing import List
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