from django.urls import path
from .views import register_view,register_view

urlpatterns = [
    path('register/', register_view, name='register_view')
]
