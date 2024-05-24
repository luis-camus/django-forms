### This project will help guide you in building forms in Django

## REQUIREMENTS
1. Install Python
2. Install Postgresql
3. Install PGadmin4
4. Use pip to install Django 'pip install django'

## How to Run the project
- Run 'python manage.py runserver' to start the server

## How to connect to your database?
- Go to settings.databases and configure your file as follows:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.<your_chosen_database>',
        'NAME': '<database_name>',
        'USER': '<database_user>',
        'PASSWORD': '<your_db_password>',
        'HOST': '<localhost || your_host>'
    }
}

## How to add a table to database
1. define a model in your models.py file.
2. run 'python manage.py makemigrations'
3. run 'python manage.py sqlmigrate <app_name> <migration_number e.g 0001>
4. run 'python manage.py migrate'
