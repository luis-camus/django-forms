from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    emp_name = forms.CharField(label='Employee Name', max_length=40, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    emp_salary = forms.IntegerField(label='Employee Salary', min_value=0, required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    emp_score = forms.FloatField(label='Employee Score')