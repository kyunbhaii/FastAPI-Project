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
# Using --prefix creates console scripts under /install/bin which we copy later.
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ----------------------------
# 2. Now copy the rest of the application code
# This layer changes frequently, so keep it after dependencies.
# ----------------------------
COPY . .

# ----------------------------------------
# Stage 2: Final Runtime Image (As Final)
# This is the clean, production-friendly image.
# Only includes what is needed to run FastAPI or Streamlit.
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
# SERVICE controls what the container runs:
# - SERVICE=app       -> start FastAPI (default)
# - SERVICE=streamlit -> start Streamlit (frontend.py)
ENV SERVICE=app

# Document the internal container ports.
# EXPOSE does not publish the port, it only documents it.
EXPOSE 8000 8501

# Entrypoint chooses which server to run based on $SERVICE.
# Use "python -m ..." only if console scripts are not found in PATH.
ENTRYPOINT ["sh", "-c", "\
  if [ \"$SERVICE\" = \"streamlit\" ]; then \
    echo \"Starting Streamlit on port ${PORT}\"; \
    # If streamlit CLI is available this will run; fallback to python -m streamlit if needed \
    (command -v streamlit >/dev/null 2>&1 && exec streamlit run frontend.py --server.port ${PORT} --server.address 0.0.0.0) || exec python -m streamlit run frontend.py --server.port ${PORT} --server.address 0.0.0.0; \
  else \
    echo \"Starting FastAPI (uvicorn) on port ${PORT}\"; \
    # run uvicorn (console script should exist). Fallback to python -m if not found. \
    (command -v uvicorn >/dev/null 2>&1 && exec uvicorn app:app --host 0.0.0.0 --port ${PORT}) || exec python -m uvicorn app:app --host 0.0.0.0 --port ${PORT}; \
  fi \
"]