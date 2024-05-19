# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port 8000 for the Django development server
EXPOSE 5000

# Run the Django development server
CMD ["flask", "run","--host=0.0.0.0", "--port=5000"]
