from typing import List
from src.schemas.department import Department
from src.models.department import Department as departmentModel

class DepartmentRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_countries(self) -> List[Department]:
        query = self.db.query(departmentModel)
        return query.all()

    def get_department(self, id: int ) -> Department:
        element = self.db.query(departmentModel).filter(departmentModel.id == id).first()
        return element
    
    def create_department(self, department: Department) -> dict:
        new_department = departmentModel(**department.model_dump())
        self.db.add(new_department)
        self.db.commit()
        self.db.refresh(new_department)
        return new_department
    
    def delete_department(self, id: int) -> dict:
        element: Department = self.db.query(departmentModel).filter(departmentModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element 