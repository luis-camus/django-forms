from django.db import models

# Create your models here.

class Position(models.Model):
    position_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.position_name
class Employee(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_gender = models.CharField(choices=gender_choices, max_length=50, null=True, blank=True)
    emp_position = models.ManyToManyField(Position, blank=True, null=True)
    emp_profile = models.ImageField(null=True, blank=True, upload_to='emp_profile_pics/')
    emp_url = models.URLField(null=True, blank=True)
    emp_email = models.EmailField(null=True, blank=True)
    emp_salary = models.IntegerField(null=False, blank=False)
    emp_files = models.FileField(null=False, blank=False, upload_to='file_uploads/')
    emp_score = models.FloatField(null=True, blank=True)
    is_employed = models.BooleanField(default=False)
    joined_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.emp_name