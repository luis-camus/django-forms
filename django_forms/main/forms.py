from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    def clean_emp_name(self):
        emp_name = self.cleaned_data.get('emp_name')
        if not emp_name.isalpha():
            raise forms.ValidationError("Employee name must contain only alphabetic characters.")
        return emp_name
    emp_name = forms.CharField(label='Employee Name', max_length=40, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    emp_profile = forms.ImageField(label='Employee Profile Picture', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))
    emp_gender = forms.ChoiceField(choices=gender_choices, label='Employee Gender', widget=forms.Select(attrs={
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
    emp_url = forms.URLField(label='Employee Profile URL', widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Add your link'
    }))
    joined_date = forms.DateTimeField(label='Date Joined:', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'datetime-local'
    }))
    emp_position = forms.ModelMultipleChoiceField(label='Employee Position', queryset=Position.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={
        'class': 'form-check-input'
    })
    )

    class Meta:
        model = Employee
        fields = [
            'emp_name',
            'emp_profile',
            'emp_gender',
            'emp_email',
            'emp_salary',
            'emp_files',
            'emp_score',
            'is_employed',
            'emp_url',
            'joined_date',
            'emp_position'
        ]