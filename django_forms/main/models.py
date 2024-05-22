from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_email = models.EmailField(null=True, blank=True)
    emp_salary = models.IntegerField(null=False, blank=False)
    emp_files = models.FileField(null=False, blank=False, upload_to='file_uploads/')
    emp_score = models.FloatField(null=True, blank=True)
    is_employed = models.BooleanField(default=False)
    joined_date = models.DateTimeField(null=True, blank=True)