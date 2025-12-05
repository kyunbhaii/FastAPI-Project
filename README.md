# FastAPI Projects Repository

A comprehensive collection of FastAPI-based applications demonstrating modern API development practices, from patient management systems to machine learning model serving. This repository showcases the versatility of FastAPI for building production-ready REST APIs and ML applications.

---

## Projects Overview

### 1. Patient Management System
A REST API for managing patient records with automatic BMI calculation and health assessments.

### 2. FastAPI ML (Machine Learning Integration)
A full-stack ML application combining FastAPI backend with Streamlit frontend for interactive model deployment.

---

## Features

### Patient Management System
* **Complete CRUD Operations**: Create, read, update, and delete patient records
* **Automatic BMI Calculation**: Computed fields for BMI and health verdict
* **Data Validation**: Robust input validation using Pydantic models
* **Sorting Capabilities**: Sort patients by height, weight, or BMI
* **JSON Storage**: Simple file-based data persistence

### FastAPI ML Application
* **Machine Learning Model Serving**: Deploy ML models via REST API
* **Interactive Frontend**: Streamlit-based UI for easy interaction
* **Real-time Predictions**: Instant model inference through API endpoints
* **Full-Stack Architecture**: Decoupled backend and frontend services

### Common Features
* **Interactive Documentation**: Auto-generated Swagger UI and ReDoc
* **Type Safety**: Full type hints and validation with Python type annotations
* **Modern Python**: Leveraging FastAPI's async capabilities

---

## 📂 Project Structure

```
FastAPI-Project/
│
├── FastAPI ML/              # ML model serving application
│   ├── backend/            # FastAPI backend service
│   ├── frontend/           # Streamlit frontend interface
│   └── models/             # Trained ML models
│
├── main.py                 # Patient management API
├── patients.json           # Patient data storage
├── requirements.txt        # Project dependencies
├── README.md              # This file
├── LICENSE                # MIT License
└── .gitignore             # Git ignore rules
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

#### 1. Clone the repository
```bash
git clone https://github.com/kyunbhaii/FastAPI-Project.git
cd FastAPI-Project
```

#### 2. Create a virtual environment
```bash
python3 -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Applications

### Patient Management System

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

**Access Points:**
* **Home**: http://127.0.0.1:8000
* **API Documentation (Swagger UI)**: http://127.0.0.1:8000/docs
* **ReDoc UI**: http://127.0.0.1:8000/redoc

### FastAPI ML Application

Navigate to the FastAPI ML directory and follow the specific instructions in its README to run both the backend and frontend services.

---

## Patient Management API Endpoints

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

## Patient Data Model

### Patient Schema
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

### patients.json Example

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

### Backend Architecture
* **Pydantic Validation**: Automatic data validation with custom constraints
* **Computed Fields**: BMI and health verdict calculated automatically
* **Atomic File Operations**: Safe concurrent file writes using temporary files
* **Type Annotations**: Full type safety with Python type hints
* **Error Handling**: Proper HTTP status codes and error messages
* **Partial Updates**: Update only specific fields without affecting others

### ML Integration
* **FastAPI Backend**: High-performance async API for model serving
* **Streamlit Frontend**: Interactive Python-based UI for model interaction
* **Model Management**: Organized structure for trained model storage
* **Scalable Architecture**: Decoupled services for easy deployment

---

## Requirements

### Core Dependencies
```txt
fastapi
uvicorn[standard]
pydantic
streamlit
```

See `requirements.txt` for complete dependency list.

---

## Future Improvements

### Completed
* Patient creation endpoints
* Update/delete routes
* Sorting functionality
* Machine learning model integration with Streamlit

### Planned
* Move from JSON to SQLite/PostgreSQL for patient data
* Add filtering by gender, age range, and city
* Implement pagination for large datasets
* Add authentication and authorization (JWT)
* Input sanitization and rate limiting
* Docker containerization for all services
* Unit and integration tests
* API versioning
* Advanced ML model deployment features
* Model monitoring and logging
* A/B testing for ML models

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

---

## Learning Resources

This repository serves as a practical learning resource for:
- Building REST APIs with FastAPI
- Implementing CRUD operations
- Data validation with Pydantic
- Serving machine learning models
- Creating interactive UIs with Streamlit
- Full-stack Python development
- Modern API documentation practices

### Tutorial Resources

This project was built following the comprehensive **CampusX FastAPI Tutorial Series**:
- [FastAPI Complete Playlist](https://youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ&si=awwdccJ3-P_NfSQz)
- An excellent resource for learning FastAPI from scratch to advanced concepts
- Covers practical implementations with real-world examples

**Highly recommended for anyone wanting to learn FastAPI!**

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- **CampusX** - Special thanks for the excellent [FastAPI Tutorial Playlist](https://youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ&si=awwdccJ3-P_NfSQz) that made this project possible

---

**⭐ If you find this project helpful, please consider giving it a star!**