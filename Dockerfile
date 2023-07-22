# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask app file and other necessary files into the container
COPY app.py requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app is running on (replace 5005 with your app's port if necessary)
EXPOSE 5005

# Command to run the Flask app when the container starts
CMD ["python", "app.py"]
