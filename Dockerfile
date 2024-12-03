FROM python:3.8-slim-buster
# Set the working directory
WORKDIR /app
# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --verbose
# Copy application code
COPY . .
COPY templates /app/templates
# Copy environment variables
COPY .venv /app/.env

# Expose port
EXPOSE 5000

# Set the working directory for the Flask app
WORKDIR /app

# Command to run the Flask app
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]