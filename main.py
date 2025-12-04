from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
import os

app = FastAPI()

# Data Validation
class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description='ID Of The Patient', example='P001')] #(... -> means these fields are required)
    name: Annotated[str, Field(..., description='Name Of The Patien', example='Anshul')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age:Annotated[int, Field(...,gt=0, lt = 120, description='Age of the patient')]
    gender: Annotated[Literal['male','female'], Field(...,description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., description='Weight of the patient in KGs')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
        
class PatientUpdate(BaseModel):
    # not adding id because it'll be provided by us(basicaly path parameter provided by us)
    name: Annotated[Optional[str], Field(default=None, description='Name Of The Patien', example='Anshul')]
    city: Annotated[Optional[str], Field(default=None, description='City where the patient is living')]
    age:Annotated[Optional[int], Field(default=None, gt=0, lt = 120, description='Age of the patient')]
    gender: Annotated[Optional[Literal['male','female']], Field(default=None, description='Gender of the patient')]
    height: Annotated[Optional[float], Field(default=None, gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[Optional[float], Field(default=None, description='Weight of the patient in KGs')]
 
def load_data():
    if not os.path.exists('patients.json'):
        return {}
    try:
        with open('patients.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}

def save_data(data):
    temp_file = 'patients_temp.json'
    final_file = 'patients.json'

    # 1) Write to temporary file first
    with open(temp_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # 2) Replace old file atomically
    os.replace(temp_file, final_file)

@app.get('/')
def info():
    return {"message": "Patient Management System API"}

@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get('/view')
def view():
    data = load_data()
    return data

# Endpoint to get a specific patient's information using a path parameter
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description = 'ID of the patient in the DB', example = 'P001')): # adding path() function
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# Using Query in Endpoint
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort by height, weight or bmi"),
    order: str = Query("asc", description="Sort in asc or desc order")
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid field. Choose from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=404,
            detail="Invalid order. Choose 'asc' or 'desc'"
        )

    data = load_data()

    reverse_order = True if order == "desc" else False

    # sort dictionary values
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse_order
    )

    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):

    # Load Dataset
    data = load_data()

    # Check If The Patient Already Exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient Already in Database')

    # New Patient Added To The Database
    data[patient.id] = patient.model_dump(exclude={'id'}) # converting pydantic object to dictonary

    # Save Into JSON file

    save_data(data)

    return JSONResponse(status_code=201, content={'message':"patiend added successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not Found')
    
    existing_patient_info = data[patient_id]

    # convert pydantic update model to dict containing only provided fields
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value 

    # inject id so we can create a Patient pydantic object and recompute bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)

    # convert back to dict and exclude id before saving
    existing_patient_info = patient_pydantic_object.model_dump(exclude={'id'})

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)
    
    return JSONResponse(status_code=200, content={'message': 'Patient Info Updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # Load Data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient Not Found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient Deleted'})