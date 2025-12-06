# FastAPI ML - Insurance Premium Category Predictor

A full-stack machine learning application that predicts insurance premium categories (Low, Medium, High) based on user demographics and health metrics. Built with FastAPI for the backend API and Streamlit for the interactive frontend.

> **Note**: This is a **learning project** created to demonstrate FastAPI implementation with machine learning models. The dataset used is **AI-generated** and not based on real-world insurance data. This project is intended for educational purposes to showcase API development, model serving, and full-stack integration.

> **Source**: This project follows the tutorial from the [CampusX FastAPI playlist](https://youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ) and implements the same concepts taught in the course.

---

## Overview

This application uses a **Random Forest Classifier** to predict insurance premium categories based on various factors including age, weight, height, income, smoking status, city, and occupation. The model achieves **90% accuracy** on test data.

### Features Engineered
- **BMI (Body Mass Index)**: Calculated from weight and height
- **Age Group**: Categorized into young, adult, middle-aged, and senior
- **Lifestyle Risk**: Assessed based on smoking status and BMI
- **City Tier**: Classified cities into Tier 1, 2, or 3

---

## Project Structure

```
FastAPI ML/
│
├── config/
│   └── city_tier.py
│
├── model/
│   ├── model.pkl
│   └── predict.py
│
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
│
├── app.py
├── frontend.py
├── ML_Model.ipynb
├── insurance.csv
├── requirements.txt
└── README.md
```

---

## Features

### Backend (FastAPI)
- RESTful `/predict` endpoint with response model validation
- `/health` endpoint for health checks and model status
- Automatic API documentation (Swagger UI)
- Data validation with Pydantic models
- Computed fields for automatic feature engineering
- Structured response with prediction confidence and class probabilities
- Model versioning support
- Organized code structure with separate modules

### Frontend (Streamlit)
- Interactive user interface
- Real-time predictions
- Input validation with proper ranges
- User-friendly form fields
- Error handling and connection checks

### Machine Learning Model
- Random Forest Classifier
- 90% accuracy on test data
- Handles categorical and numerical features
- OneHotEncoding for categorical variables
- Scikit-learn pipeline for preprocessing

---

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

---

## Installation

### 1. Navigate to the project directory
```bash
cd "FastAPI ML"
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install fastapi==0.121.0 uvicorn==0.38.0 streamlit==1.52.0 pandas==2.3.0 scikit-learn==1.7.0 pydantic==2.12.3 requests==2.32.4
```

---

## Running the Application

You need to run both the backend and frontend services. Open **two terminal windows**:

### Terminal 1: Start the FastAPI Backend

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:
- **API Base**: http://127.0.0.1:8000
- **Swagger UI**: http://127.0.0.1:8000/docs
- **Prediction Endpoint**: http://127.0.0.1:8000/predict

### Terminal 2: Start the Streamlit Frontend

```bash
streamlit run frontend.py
```

The Streamlit app will open automatically in your browser at:
- **Frontend**: http://localhost:8501

---

## API Documentation

### Health Check Endpoint
```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "model_loaded": true
}
```

### Prediction Endpoint
```http
POST /predict
```

**Request Body:**
```json
{
  "age": 35,
  "weight": 75.0,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "predicted_category": "Low",
  "confidence": 0.8432,
  "class_probabilities": {
    "Low": 0.8432,
    "Medium": 0.1234,
    "High": 0.0334
  }
}
```

### Input Validation

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `age` | int | 1-119 | Age of the user |
| `weight` | float | > 0 | Weight in kilograms |
| `height` | float | 0-2.5 | Height in meters |
| `income_lpa` | float | > 0 | Annual income in LPA |
| `smoker` | bool | true/false | Smoking status |
| `city` | string | Any city name | City of residence |
| `occupation` | string | See below | User's occupation |

**Valid Occupations:**
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

---

## Usage Examples

### Using the Streamlit UI
1. Open http://localhost:8501 in your browser
2. Fill in your personal details:
   - Age, Weight, Height
   - Annual Income
   - Smoking status
   - City and Occupation
3. Click **"Predict Premium Category"**
4. View your predicted insurance premium category

### Using the API Directly

#### cURL Example
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "weight": 75.0,
    "height": 1.75,
    "income_lpa": 12.5,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }'
```

#### Python Example
```python
import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "age": 35,
    "weight": 75.0,
    "height": 1.75,
    "income_lpa": 12.5,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

response = requests.post(url, json=data)
result = response.json()
print(f"Predicted Category: {result['predicted_category']}")
```

---

## Model Details

### Algorithm
- **Type**: Random Forest Classifier
- **Framework**: Scikit-learn
- **Task**: Multi-class Classification (Low, Medium, High)

### Features Used
1. **BMI**: Computed from weight/height²
2. **Age Group**: Categorical (young, adult, middle_aged, senior)
3. **Lifestyle Risk**: Categorical (low, medium, high)
4. **City Tier**: Numerical (1, 2, or 3)
5. **Income (LPA)**: Numerical
6. **Occupation**: Categorical

### City Tier Classification

**Tier 1 Cities:**
Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune

**Tier 2 Cities:**
Jaipur, Chandigarh, Indore, Lucknow, Patna, Ranchi, Visakhapatnam, Coimbatore, Bhopal, Nagpur, Vadodara, Surat, Rajkot, Jodhpur, Raipur, Amritsar, Varanasi, Agra, Dehradun, Mysore, Jabalpur, Guwahati, Thiruvananthapuram, Ludhiana, Nashik, Allahabad, Udaipur, Aurangabad, Hubli, Belgaum, Salem, Vijayawada, Tiruchirappalli, Bhavnagar, Gwalior, Dhanbad, Bareilly, Aligarh, Gaya, Kozhikode, Warangal, Kolhapur, Bilaspur, Jalandhar, Noida, Guntur, Asansol, Siliguri

**Tier 3 Cities:** All other cities

### Performance Metrics
- **Accuracy**: 90% on test set
- **Test Split**: 80/20 train-test split
- **Random State**: 42 for reproducibility

### Training Dataset
- **Source**: insurance.csv (AI-generated for educational purposes)
- **Size**: 100 samples
- **Features**: 8 columns
- **Target**: insurance_premium_category (Low, Medium, High)
- **Note**: This is synthetic data created for learning FastAPI implementation. For production use, train on real-world insurance datasets.

---

## Important Disclaimers

### Educational Purpose
This project is designed as a **learning exercise** to demonstrate:
- FastAPI backend development and API design
- Machine learning model integration with web APIs
- Streamlit frontend development
- Full-stack application architecture
- Pydantic data validation
- Model serialization and deployment

### Dataset Limitations
- The insurance dataset is **AI-generated** and does not represent real-world insurance pricing
- Model predictions should **not be used** for actual insurance decisions
- The dataset is intentionally small (100 samples) for learning purposes
- Feature relationships are simplified for educational demonstration

### For Production Use
If you want to build a production-ready insurance premium predictor:
- Obtain real-world insurance datasets (e.g., from Kaggle, UCI ML Repository, or insurance providers)
- Expand the dataset to include more samples (typically thousands or more)
- Perform thorough feature engineering and domain research
- Conduct proper model validation and testing
- Implement bias detection and fairness checks
- Ensure compliance with insurance regulations and data privacy laws
- Add comprehensive error handling and logging
- Implement proper security measures

Feel free to **use this codebase as a template** and train your own model with real data!

---

## Model Training

The model was trained using the Jupyter notebook `ML_Model.ipynb`. Key steps:

1. **Data Loading**: Load insurance data from CSV
2. **Feature Engineering**: Create BMI, age_group, lifestyle_risk, city_tier
3. **Preprocessing**: OneHotEncoding for categorical features
4. **Model Training**: Random Forest with 100 estimators
5. **Evaluation**: Achieved 90% accuracy
6. **Model Saving**: Exported as `model.pkl` using pickle

To retrain the model:
```bash
jupyter notebook ML_Model.ipynb
```

---

## Technical Implementation

### Project Architecture

The project follows a modular architecture with clear separation of concerns:

**config/** - Configuration files
- `city_tier.py`: Contains tier 1 and tier 2 city lists for classification

**model/** - Machine learning model and prediction logic
- `model.pkl`: Serialized Random Forest model
- `predict.py`: Model loading and prediction function with confidence scores

**schema/** - Pydantic models for data validation
- `user_input.py`: Input validation with computed fields for feature engineering
- `prediction_response.py`: Response model with prediction details

**app.py** - FastAPI application with route handlers

**frontend.py** - Streamlit UI for user interaction

### Pydantic Model with Computed Fields

The API uses Pydantic's `@computed_field` decorator for automatic feature engineering:

```python
@computed_field
@property
def bmi(self) -> float:
    return self.weight / (self.height ** 2)

@computed_field
@property
def lifestyle_risk(self) -> str:
    if self.smoker and self.bmi > 30:
        return "high"
    elif self.smoker or self.bmi > 27:
        return "medium"
    else:
        return "low"
```

The `user_input.py` also includes field validators:

```python
@field_validator('city')
@classmethod
def normalize_city(cls, v: str) -> str:
    return v.strip().title()
```

This ensures that features are consistently computed for both training and prediction, and city names are normalized.

### Response Model

The API returns structured responses with confidence scores:

```python
class PredictionResponse(BaseModel):
    predicted_category: str
    confidence: float
    class_probabilities: Dict[str, float]
```

---

## Troubleshooting

### Common Issues

**Backend won't start:**
- Check if port 8000 is already in use
- Verify `model/model.pkl` file exists in the directory
- Ensure all dependencies are installed
- Check that all required folders (config, model, schema) are present

**Frontend can't connect to backend:**
- Ensure backend is running on port 8000
- Check the API_URL in frontend.py matches your backend
- Verify both services are running simultaneously

**"Could not connect to the FastAPI server" error:**
- Make sure you started the FastAPI backend first
- Check if the backend is accessible at http://127.0.0.1:8000

**Invalid predictions:**
- Verify input data format matches the expected types
- Check that city and occupation values are valid
- Ensure numeric values are within acceptable ranges

---

## Dependencies

From `requirements.txt`:
```txt
fastapi==0.121.0
uvicorn==0.38.0
starlette==0.49.3

pydantic==2.12.3
pandas==2.3.0
numpy==2.2.6
scikit-learn==1.7.0

streamlit==1.52.0
requests==2.32.4
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Expand training dataset for better generalization
- Add probability scores to predictions
- Implement model versioning
- Add user authentication
- Deploy to cloud (Heroku, AWS, or Azure)
- Add more features (medical history, family history)
- Implement A/B testing for model improvements
- Add data visualization in frontend
- Create Docker containers for easy deployment
- Add unit and integration tests

---

## Learning Resources

This project was built as a learning exercise using resources from:
- [CampusX FastAPI Playlist](https://youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ) - Primary learning resource
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

### Learning Objectives Achieved
- Understanding FastAPI framework fundamentals
- Implementing REST API endpoints with proper validation
- Integrating machine learning models with web APIs
- Using Pydantic for data validation and computed fields
- Building interactive frontends with Streamlit
- Model serialization and deployment
- Full-stack application development
- Project organization with modular architecture
- Response models with confidence scores and probabilities

## License

This project is part of the FastAPI-Project repository and is available under the MIT License.

## Acknowledgments

- **CampusX** for the excellent FastAPI tutorials

**If you find this project helpful, please star the main repository!**

[← Back to Main Repository](https://github.com/kyunbhaii/FastAPI-Project)
