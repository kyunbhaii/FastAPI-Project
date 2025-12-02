from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

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