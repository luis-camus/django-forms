from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    emp_name = forms.CharField(label='Employee Name', max_length=40, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    emp_email = forms.EmailField(label='Employee Email', widget=forms.EmailInput(attrs={
        'type': 'email',
        'class': 'form-control'
    }))
    emp_salary = forms.IntegerField(label='Employee Salary', min_value=0, required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    emp_files = forms.FileField(label='Upload Employee File', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))
    emp_score = forms.FloatField(label='Employee Score', max_value=10, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    is_employed = forms.BooleanField(label='is Employed?', widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    joined_date = forms.DateTimeField(label='Date Joined:', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'datetime-local'
    }))