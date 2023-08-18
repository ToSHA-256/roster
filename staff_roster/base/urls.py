from django.urls import path
from .views import index,roster

urlpatterns = [
    path('', index, name='index'),
    path('roster/', roster, name='roster')
]
