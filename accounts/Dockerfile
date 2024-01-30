# Dockerfile in accounts directory
FROM python:3.9-slim

WORKDIR /app

# Copy the entire contents of the priceoye directory into the container at /app/
COPY ../ /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Your remaining Dockerfile instructions
