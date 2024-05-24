from django.core.exceptions import ValidationError
#in this file, we declare the validations for our forms that we can pass into our models.py file to validate a specific row in our model
def validate_emp_name(value):
    if not value.isalpha():
        raise ValidationError(
            '%(value)s is not a valid name. Employee name should only contain alphabetic characters.',
            params={'value': value},
        )