from django.contrib import admin
from .models import Employee, Position
# Register your models here.

# we register our models here so that we can access and test it on Django Admin Panel
admin.site.register(Employee)
admin.site.register(Position)