from django.db import models
from .validators import validate_emp_name
# Create your models here.

# this is also the file that we use to define our database table
# with Django's ORM, once we change something here we just have to run 'python manage.py makemigrations' then 'python manage.py migrate'


class Position(models.Model):
    position_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.position_name
class Employee(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    #character field
    emp_name = models.CharField(max_length=50, null=False, blank=False, validators=[validate_emp_name])

    #choice field - we also have to define a tuple inside this file so we can pass it as choices in the declaration.
    emp_gender = models.CharField(choices=gender_choices, max_length=50, null=True, blank=True)

    #ManyToManyFIeld - we use this if one of our values is directly linked to another table in our database e.g position model
    emp_position = models.ManyToManyField(Position, blank=True, null=True)

    #ImageField - we also have to pass in our target directory in upload_to to save the images passed locally
    emp_profile = models.ImageField(null=True, blank=True, upload_to='emp_profile_pics/')

    #URLField - for handling URLS on forms
    emp_url = models.URLField(null=True, blank=True)

    #email field for handling email input
    emp_email = models.EmailField(null=True, blank=True)

    #Integer Field - we use this for handling whole numbers
    emp_salary = models.IntegerField(null=False, blank=False)

    #filefield - this one's for handling file input
    emp_files = models.FileField(null=False, blank=False, upload_to='file_uploads/')

    #FolatField - we use this for handling numbers that contains decimal places
    emp_score = models.FloatField(null=True, blank=True)
    
    #BooleanField - we use this to handle boolean values e.g. True or False
    is_employed = models.BooleanField(default=False)

    #DateTimeField - we use this for handling date time values
    joined_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.emp_name