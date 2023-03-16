import uvicorn
from bson import ObjectId
from typing import Optional
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.collection import Collection
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["hrms"]
collection: Collection = db["employees"]


class EmployeeInDB(BaseModel):
    """
    A Pydantic model representing an employee in the database.

    Attributes:
    -----------
    id : Optional[str]
        The ID of the employee in the database.
    name : str
        The name of the employee.
    salary : float
        The salary of the employee.
    age : float
        The age of the employee.
    """

    id: Optional[str]
    name: str
    salary: float
    age: float


class Employee(BaseModel):
    """
    A Pydantic model representing an employee.

    Attributes:
    -----------
    name : str
        The name of the employee.
    salary : float
        The salary of the employee.
    age : float
        The age of the employee.
    """

    name: str
    salary: float
    age: float


@app.get("/employee")
async def get_employees():
    """
    Get a list of all employees in the database.

    Returns:
    --------
    List[EmployeeInDB]:
        A list of EmployeeInDB objects representing the employees in the database.
    """
    cursor = collection.find({})
    employees = []
    for employee in cursor:
        # Convert the ObjectId to a string and add it to the employee dictionary
        employee["id"] = str(employee["_id"])
        # Create an EmployeeInDB object from the employee dictionary and add it to the list
        employees.append(EmployeeInDB(**employee))
    return employees


@app.post("/employee")
async def create_employee(employee: Employee):
    """
    Create a new employee in the database.

    Parameters:
    -----------
    employee : Employee
        An Employee object representing the new employee.

    Returns:
    --------
    JSONResponse:
        A JSONResponse object representing the newly created employee.
    """
    employee_data = jsonable_encoder(employee)
    result = collection.insert_one(employee_data)
    created_employee = collection.find_one({"_id": result.inserted_id})
    # Convert the ObjectId to a string and add it to the employee dictionary
    created_employee["id"] = str(created_employee["_id"])
    return JSONResponse(content=created_employee)


@app.put("/employee/{employee_id}")
async def update_employee(employee_id: str, employee: Employee):
    """
    Update an employee in the database.

    Parameters:
    -----------
    employee_id : str
        The ID of the employee to update.
    employee : Employee
        An Employee object representing the updated employee data.

    Returns:
    --------
    EmployeeInDB:
        An EmployeeInDB object representing the updated employee.
    """
    obj_id = ObjectId(employee_id)
    employee_data = jsonable_encoder(employee)
    updated_employee = collection.find_one_and_update(
        {"_id": obj_id}, {"$set": employee_data}, return_document=True
    )
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    # Convert the ObjectId to a string and add it to the employee dictionary
    updated_employee["id"] = str(updated_employee["_id"])
    return updated_employee


@app.delete("/employee/{employee_id}")
async def delete_employee(employee_id: str):
    """
    Delete an employee in the database.

    Parameters:
    -----------
    employee_id : str
        The ID of the employee to update.

    Returns:
    --------
    dict:
        {"message": "Record deleted"}.
    """
    obj_id = ObjectId(employee_id)
    result = collection.delete_one({"_id": obj_id})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Record deleted"}


if __name__ == "__main__":
    uvicorn.run(app)
