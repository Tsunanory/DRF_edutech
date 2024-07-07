FROM python:3

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
       postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Copy wait script
COPY wait-for-db.sh .

# Make sure wait script is executable
RUN chmod +x wait-for-db.sh

# Set environment variables
ENV CELERY_BROKER_URL=redis://redis:6379/0
ENV CELERY_RESULT_BACKEND=redis://redis:6379/0
ENV DJANGO_SETTINGS_MODULE=config.settings

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["./wait-for-db.sh", "db", "python", "manage.py", "runserver", "0.0.0.0:8000"]
