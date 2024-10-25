# Dockerfile
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ./app/requirements.txt ./requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY ./app /app

# Command to run the application
CMD ["python", "app.py"]


