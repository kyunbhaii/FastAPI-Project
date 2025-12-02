# FastAPI Patient Management System

A lightweight FastAPI-based backend project designed for learning, experimenting, and building APIs using Python.

---

## Features

* View and manage patient data (JSON-based storage)
* Clean routing structure
* Easily extendable with new API features
* Modern FastAPI tooling and documentation support

---

## Project Structure

```
FastAPI/
│── main.py
│── patient.json
│── README.md
│── requirements.txt
│── .gitignore
```

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
source myvenv/bin/activate
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

Visit:

* Home: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* API Documentation (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## patient.json Example

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
  }
}
```

---

## Future Improvements

* Add patient creation endpoints
* Add update/delete routes
* Filtering by gender, BMI range, or city
* Move from JSON to SQLite/PostgreSQL
* Authentication (JWT)
* Full frontend UI

---

## License

This project is open-source and available under the MIT License.
