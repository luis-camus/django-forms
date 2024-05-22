from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
def home(request):
    return render(request, 'main/home.html')

def employee_data(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['emp_name']
            emp_email = form.cleaned_data['emp_email']
            salary = form.cleaned_data['emp_salary']
            emp_files = form.cleaned_data['emp_files']
            score = form.cleaned_data['emp_score']
            is_employed = form.cleaned_data['is_employed']
            joined_date = form.cleaned_data['joined_date']
            emp = Employee.objects.create(
                emp_name=name,
                emp_email=emp_email,
                emp_salary=salary,
                emp_files=emp_files, 
                emp_score=score, 
                is_employed=is_employed,
                joined_date=joined_date)
            emp.save()
            return HttpResponse("data is saved in database")
    form = EmployeeForm()
    return render(request, 'main/employee.html', {'form': form})
# Create your views here.
