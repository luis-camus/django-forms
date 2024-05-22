from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('employee/', views.employee_data, name='employee')
]