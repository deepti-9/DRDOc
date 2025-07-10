# Use a slim Python base image
FROM python:3.10-slim

# Set environment variable to avoid Python buffering issues
ENV PYTHONUNBUFFERED=1

# Create a working directory
WORKDIR /application_portal

# Install system dependencies (optional: for psycopg2, Pillow, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
    pkg-config \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .



# Expose port 8000
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
