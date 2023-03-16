# FastAPI MongoDB CRUD
![made-with-python](https://img.shields.io/badge/Made%20with-Python-0078D4.svg)
![fastapi](https://img.shields.io/badge/Fastapi-109989?logo=FASTAPI&logoColor=white)
![mongodb](https://img.shields.io/badge/MongoDB-4EA94B?logo=mongodb&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

This repository contains a simple implementation of a RESTful API using the FastAPI framework in Python. The API allows CRUD operations (Create, Read, Update, Delete) on employee data stored in a MongoDB database. The code utilizes the Pydantic library for data validation and MongoDB's PyMongo driver for database interactions. The API provides endpoints for retrieving all employees, creating a new employee, updating an existing employee, and deleting an employee by ID.

## Installation
Open command prompt and create new environment
```
conda create -n your_env_name python = (any_version_number > 3.10)
```
Then Activate the newly created environment
```
conda activate your_env_name
```
Clone the repository using `git`
```
git clone https://github.com/Prakashdeveloper03/FastAPI-MongoDB-CRUD.git
```
Change to the cloned directory
```
cd <directory_name>
```
Then install all requirement packages for the app
```
pip install -r requirements.txt
```
Then, Run the `main.py` script
```
python main.py
```
## 📷 Screenshots
![swagger_image](markdown/interface.png)