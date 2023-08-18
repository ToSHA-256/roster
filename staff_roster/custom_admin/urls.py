from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_sectors/', views.get_sectors, name='get_sectors'),
    path('employee_form/', views.employee_form, name='employee_form'),
]
