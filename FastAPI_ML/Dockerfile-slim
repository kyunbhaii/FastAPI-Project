# ----------------------------------------
# Stage 1: Builder Stage
# This stage installs all dependencies.
# We keep it separate so the final image stays small.
# ----------------------------------------
FROM python:3.10-slim AS builder

# Set working directory inside container.
WORKDIR /app

# (Optional) Install build tools only if needed
# RUN apt-get update && apt-get install -y build-essential gcc

# ----------------------------
# 1. Copy only requirements first
# This helps Docker cache the dependency layer.
# ----------------------------
COPY requirements.txt .

# Install dependencies into a temporary folder.
# These installed deps will be copied into the final image only.
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ----------------------------
# 2. Now copy the rest of the application code
# This layer changes frequently, so keep it after dependencies.
# ----------------------------
COPY . .


# ----------------------------------------
# Stage 2: Final Runtime Image (As Final)
# This is the clean, production-friendly image.
# Only includes what is needed to run FastAPI.
# ----------------------------------------
FROM python:3.10-slim AS final

# Set working directory inside container.
WORKDIR /app

# Copy installed dependencies from the builder stage.
# /install contains site-packages and scripts.
COPY --from=builder /install /usr/local

# Copy the application source code.
COPY --from=builder /app /app

# Default environment variable (runtime can override it)
ENV PORT=8000

# Document the internal container port.
EXPOSE 8000

# Start FastAPI app with Uvicorn.
# "app:app" refers to app.py (file) and app (FastAPI instance).
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]