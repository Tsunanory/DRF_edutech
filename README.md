Edutech project

DRF1 Project

This is a Django REST Framework (DRF) project named DRF1. It includes two main apps, users and materials, and utilizes Celery for background task processing and Redis as a message broker. The project is containerized using Docker and Docker Compose.

Project Structure

markdown
Copy code
DRF1/
├── celerybeat-schedule
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── yasg.py
├── docker-compose.yaml
├── dockerfile
├── edutech_app.json
├── manage.py
├── materials
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_course_owner_lesson_owner.py
│   │   ├── 0003_subscription.py
│   │   └── __init__.py
│   ├── models.py
│   ├── paginators.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── stripe_views.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   ├── validators.py
│   └── views.py
├── media
├── requirements.txt
├── static
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── fixtures
│   │   └── groups.json
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       ├── __init__.py
│   │       ├── create_moderator_group.py
│   │       └── csu.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_user_username_user_avatar_user_city_and_more.py
│   │   ├── 0003_payment.py
│   │   ├── 0004_alter_payment_options.py
│   │   ├── 0005_alter_user_groups_alter_user_user_permissions_and_more.py
│   │   └── __init__.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
└── wait-for-db.sh
Prerequisites

Docker
Docker Compose
Setup Instructions

1. Clone the Repository
sh
Copy code
git clone <repository-url>
cd DRF1
2. Create Environment Variables File
Create a .env file in the project root and add the following environment variables:

env
Copy code
DEBUG=True
SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DATABASE_URL=postgres://postgres:password@db:5432/drf1
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
POSTGRES_DB=drf1
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
EMAIL_HOST_USER=your_email@yandex.ru
EMAIL_HOST_PASSWORD=your_email_password
3. Build and Run Docker Containers
Build and run the Docker containers using Docker Compose:

sh
Copy code
docker-compose up --build
4. Run Database Migrations
Open a new terminal window and run the following command to apply database migrations:

sh
Copy code
docker-compose exec web python manage.py migrate
5. Create a Superuser
Create a superuser to access the Django admin interface:

sh
Copy code
docker-compose exec web python manage.py createsuperuser
6. Collect Static Files
If your project requires static files, run the following command:

sh
Copy code
docker-compose exec web python manage.py collectstatic
7. Access the Application
Open your web browser and visit http://localhost:8000 to access the Django application.

Running Celery

Celery is configured to run with Redis as the broker. The following services are included in the Docker Compose setup:

celery: Celery worker
celery-beat: Celery beat scheduler
Running Celery Commands
You can run additional Celery commands using Docker Compose. For example, to start a Celery worker:

sh
Copy code
docker-compose exec celery celery -A config worker --loglevel=info
To start the Celery beat scheduler:

sh
Copy code
docker-compose exec celery-beat celery -A config beat --loglevel=info
