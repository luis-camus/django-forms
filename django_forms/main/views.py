from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
def home(request):
    return render(request, 'main/home.html')

def employee_data(request):

    if request.method == 'POST': #checks the method of the request, if it's POST then it would process post request
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid(): # this line checks if form is valid
            form.save() #if the form's valid it's gonna call the save method to save it to your database

             
            # Below this line is how it looks like before if you were not to declare a Meta in forms.py file.
            
            # Declaring a Meta in your forms.py file will save you alot of lines here in views.py file


            # name = form.cleaned_data['emp_name']
            # emp_gender = form.cleaned_data['emp_gender']
            # profile_photo = form.cleaned_data['emp_profile']
            # emp_email = form.cleaned_data['emp_email']
            # salary = form.cleaned_data['emp_salary']
            # emp_files = form.cleaned_data['emp_files']
            # score = form.cleaned_data['emp_score']
            # is_employed = form.cleaned_data['is_employed']
            # emp_url = form.cleaned_data['emp_url']
            # joined_date = form.cleaned_data['joined_date']
            # emp = Employee.objects.create(
            #     emp_name=name,
            #     emp_gender=emp_gender,
            #     emp_profile=profile_photo,
            #     emp_email=emp_email,
            #     emp_salary=salary,
            #     emp_files=emp_files, 
            #     emp_score=score, 
            #     is_employed=is_employed,
            #     emp_url=emp_url,
            #     joined_date=joined_date)
            # emp.save()
            return HttpResponse("data is saved in database")
        else:
            pass
    form = EmployeeForm() 

# if the request is GET and not post it would just return the line below
# that would render the web page consisting the form cause we passed in the form to it
    return render(request, 'main/employee.html', {'form': form})
# Create your views here.
