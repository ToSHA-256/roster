from django.urls import path
from .views import index, roster, management_list

urlpatterns = [
    path('', index, name='index'),
    path('roster/', roster, name='roster'),
    path('managements/', management_list, name='management_list'),
    path('<int:management_id>/departments/', management_list, name='department_list'),
    path('managements/add/', management_list, name='management_add_view'),
]
