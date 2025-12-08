# Use a small, production-friendly Python base image.
FROM python:3.10-slim

# Set working directory inside container.
WORKDIR /app

# ----------------------------
# 1. Copy only requirements first
# This helps Docker cache the dependency layer.¯
# ----------------------------
COPY requirements.txt .

# Install dependencies.
# This layer will be reused unless requirements.txt changes.
RUN pip install --no-cache-dir -r requirements.txt

# ----------------------------
# 2. Now copy the rest of the application code
# This layer changes frequently, so keep it after dependencies.
# ----------------------------
COPY . .

# Default environment variable (runtime can override it)
ENV PORT=8000

# Document the internal container port.
EXPOSE 8000

# Start FastAPI app with Uvicorn.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]