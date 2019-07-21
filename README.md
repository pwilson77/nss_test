# nss_test

This project loads Microsoft Excel file data and uploads it into the Django Database.

### The project has the following dependencies

1. Python Django
2. Celery
3. Openpyxl
4. RabbitMQ (as the worker for Celery)

### To run the project

1. **_git clone _** this repo
2. Install the above dependencies
3. Run **_python manage.py makemigrations_**
4. Run **_python manage.py migrate_**
5. Finally run **_python manage.py runserver_**, to start the server

### Please note there is sample excel file in the folder excel_files
