# Choose the base Python environment the container will use.
# This image includes Python 3.10 with a lightweight Debian system (slim),
# which keeps the Docker image small and suitable for production.
FROM python:3.10-slim

# Set the working directory inside the container.
# All commands after this will run inside /app and all file copies will be placed here.
WORKDIR /app

# Copy all project files from the local machine into the /app directory inside the container.
# This includes Python files, model files, requirements.txt, and any additional resources.
COPY . /app

# Install all Python dependencies listed in requirements.txt.
# --no-cache-dir prevents pip from storing cache, keeping the image size smaller.
RUN pip install --no-cache-dir -r requirements.txt

# Document that the application inside the container will listen on port 8000.
# This does NOT expose the port externally; that happens when running the container using -p.
EXPOSE 8000

# Start the FastAPI application using Uvicorn when the container launches.
# "app:app" refers to app.py (file) and app (FastAPI instance).
# Host 0.0.0.0 ensures the API is accessible outside the container.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]