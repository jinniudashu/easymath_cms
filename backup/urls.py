from django.urls import path
from .views import data_backup

urlpatterns = [
    path('data_backup/', data_backup, name='data_backup'),
]