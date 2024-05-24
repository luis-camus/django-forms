from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    # tuple is also declared here so that we can access it too in our frontend
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    # In the widget, we can declare attributes such as classes so we can add custom css to each element

    # Character Field
    emp_name = forms.CharField(label='Employee Name', max_length=40, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    # Image Field
    emp_profile = forms.ImageField(label='Employee Profile Picture', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))

    # Choice Field
    emp_gender = forms.ChoiceField(choices=gender_choices, label='Employee Gender', widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    # Email Field
    emp_email = forms.EmailField(label='Employee Email', widget=forms.EmailInput(attrs={
        'type': 'email',
        'class': 'form-control'
    }))   

    # Integer Field 
    emp_salary = forms.IntegerField(label='Employee Salary', min_value=0, required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    #File Field
    emp_files = forms.FileField(label='Upload Employee File', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))

    #Float Field
    emp_score = forms.FloatField(label='Employee Score', max_value=10, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    # Boolean Field
    is_employed = forms.BooleanField(label='is Employed?', widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))

    # Url Field
    emp_url = forms.URLField(label='Employee Profile URL', widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Add your link'
    }))

    # DateTime Field
    joined_date = forms.DateTimeField(label='Date Joined:', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'datetime-local'
    }))

    # Multiple Choice Field
    emp_position = forms.ModelMultipleChoiceField(label='Employee Position', queryset=Position.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={
        'class': 'form-check-input'
    })
    )

    # the class Meta below acts as a constructor on what order we want our forms to be rendered
    # Also used to construct the post object for passing data from request to database
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