# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /API

# Copy the current directory contents into the container at /app
COPY . /API

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r API/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "api.py"]
