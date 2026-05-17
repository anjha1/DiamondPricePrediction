# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy project files to container
COPY . /app/

# Install system dependencies (if needed for any packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variable to not buffer Python output
ENV PYTHONUNBUFFERED=1

# Run the Flask application
CMD ["python", "app.py"]
