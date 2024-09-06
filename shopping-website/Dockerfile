# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir Werkzeug==2.0.3

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=shopping_cart
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=rootpassword

# Run app.py when the container launches
CMD ["python", "app.py"]

