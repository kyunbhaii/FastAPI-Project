# FastAPI Patient Management System

A comprehensive FastAPI-based REST API for managing patient records with automatic BMI calculation and health verdicts. This project demonstrates modern API development practices with data validation, CRUD operations, and JSON-based persistence.

---

## Features

* **Complete CRUD Operations**: Create, read, update, and delete patient records
* **Automatic BMI Calculation**: Computed fields for BMI and health verdict
* **Data Validation**: Robust input validation using Pydantic models
* **Sorting Capabilities**: Sort patients by height, weight, or BMI
* **JSON Storage**: Simple file-based data persistence
* **Interactive Documentation**: Auto-generated Swagger UI and ReDoc
* **Type Safety**: Full type hints and validation with Python type annotations

---

## Project Structure

```
FastAPI/
│── main.py
│── patients.json
│── README.md
│── requirements.txt
└── .gitignore
```

---

## API Endpoints

### Information Endpoints
* `GET /` - API welcome message
* `GET /about` - API description
* `GET /view` - View all patients

### Patient Operations
* `GET /patient/{patient_id}` - Get specific patient details
* `POST /create` - Add a new patient
* `PUT /edit/{patient_id}` - Update patient information
* `DELETE /delete/{patient_id}` - Remove a patient

### Data Queries
* `GET /sort` - Sort patients by height, weight, or BMI (ascending/descending)

---

## Installation

### 1. Clone this repository
```bash
git clone https://github.com/your-username/FastAPI-Project.git
cd FastAPI-Project
```

### 2. Create a virtual environment
```bash
python3 -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

### Access Points:
* **Home**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **API Documentation (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Usage Examples

### Create a New Patient
```bash
curl -X POST "http://127.0.0.1:8000/create" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "P001",
    "name": "Anshul Kumar",
    "city": "Prayagraj",
    "age": 25,
    "gender": "male",
    "height": 1.75,
    "weight": 70.0
  }'
```

### Get Patient Details
```bash
curl "http://127.0.0.1:8000/patient/P001"
```

### Update Patient Information
```bash
curl -X PUT "http://127.0.0.1:8000/edit/P001" \
  -H "Content-Type: application/json" \
  -d '{
    "weight": 72.5,
    "city": "Allahabad"
  }'
```

### Sort Patients
```bash
curl "http://127.0.0.1:8000/sort?sort_by=bmi&order=desc"
```

### Delete a Patient
```bash
curl -X DELETE "http://127.0.0.1:8000/delete/P001"
```

---

## Data Models

### Patient Model
- **id**: Unique patient identifier (e.g., "P001")
- **name**: Patient's full name
- **city**: City of residence
- **age**: Age (1-119 years)
- **gender**: "male" or "female"
- **height**: Height in meters (must be positive)
- **weight**: Weight in kilograms
- **bmi**: Automatically calculated Body Mass Index
- **verdict**: Health category based on BMI
  - Underweight: BMI < 18.5
  - Normal: 18.5 ≤ BMI < 25
  - Overweight: 25 ≤ BMI < 30
  - Obese: BMI ≥ 30

---

## patients.json Example

```json
{
  "P001": {
    "name": "Ananya Sharma",
    "city": "Guwahati",
    "age": 28,
    "gender": "female",
    "height": 1.65,
    "weight": 90.0,
    "bmi": 33.06,
    "verdict": "Obese"
  },
  "P002": {
    "name": "Rahul Verma",
    "city": "Mumbai",
    "age": 35,
    "gender": "male",
    "height": 1.80,
    "weight": 75.0,
    "bmi": 23.15,
    "verdict": "Normal"
  }
}
```

---

## Technical Highlights

* **Pydantic Validation**: Automatic data validation with custom constraints
* **Computed Fields**: BMI and health verdict calculated automatically
* **Atomic File Operations**: Safe concurrent file writes using temporary files
* **Type Annotations**: Full type safety with Python type hints
* **Error Handling**: Proper HTTP status codes and error messages
* **Partial Updates**: Update only specific fields without affecting others

---

## Requirements

```txt
fastapi
uvicorn[standard]
pydantic
```

---

## Future Improvements

* ~~Add patient creation endpoints~~ (Completed)
* ~~Add update/delete routes~~ (Completed)
* ~~Filtering by gender, BMI range, or city~~ (Sorting implemented)
* Move from JSON to SQLite/PostgreSQL
* Add filtering by gender, age range, and city
* Implement pagination for large datasets
* Add authentication and authorization (JWT)
* Input sanitization and rate limiting
* Full frontend UI (React/Vue.js)
* Docker containerization
* Unit and integration tests
* API versioning

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## License

This project is open-source and available under the MIT License.
