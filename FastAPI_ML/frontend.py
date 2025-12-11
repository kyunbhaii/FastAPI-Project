# frontend.py
import os
import streamlit as st
import requests

# Read API base URL from environment; default to service name 'app' (Compose DNS)
API_BASE = os.getenv("API_URL", "http://app:8000")
PREDICT_ENDPOINT = f"{API_BASE.rstrip('/')}/predict"  # ensure single slash

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job",
    ],
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post(PREDICT_ENDPOINT, json=input_data, timeout=10)
    except requests.exceptions.ConnectionError:
        st.error(f"❌ Could not connect to the FastAPI server at {PREDICT_ENDPOINT}. Make sure it's reachable from this container.")
    except requests.exceptions.Timeout:
        st.error(f"❌ Request to {PREDICT_ENDPOINT} timed out.")
    else:
        # Try parse JSON
        try:
            result = response.json()
        except Exception:
            st.error("Invalid JSON response from API.")
            st.write(response.text)
        else:
            if response.status_code == 200:
                # Expected shape: {"predicted_category": "..."}
                if isinstance(result, dict) and "predicted_category" in result:
                    pred = result["predicted_category"]
                    st.success(f"Predicted Insurance Premium Category: **{pred}**")
                else:
                    st.error("API returned 200 but response shape was unexpected.")
                    st.write(result)
            else:
                st.error(f"API Error: {response.status_code}")
                st.write(result)