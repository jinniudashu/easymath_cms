from django.urls import path
from .views import courses_list, units_list, lessons_list, exercises_list

urlpatterns = [
    path('courses/', courses_list, name='courses'),
    path('units/', units_list, name='units'),
    path('lessons/', lessons_list, name='lessons'),
    path('exercises/', exercises_list, name='exercises'),
]