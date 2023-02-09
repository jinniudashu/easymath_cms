from django.urls import path
from .views import courses_list, units_list, lessons_all, lessons_list, unit_lessons_list, lesson_detail, exercises_list

urlpatterns = [
    path('', courses_list, name='courses'),  # 所有系列课
    path('lessons/', lessons_all, name='lessons_all'),  # 所有课程视频
    path('<int:pk>/units/', units_list, name='units'),  # 某系列课的所有单元
    path('<int:pk>/lessons/', lessons_list, name='lessons'),  # 某系列课的所有视频课
    path('<int:cpk>/units/<int:upk>/lessons/', unit_lessons_list, name='unit_lessons'),  # 某系列课的某单元的所有视频课
    path('lessons/<int:pk>/', lesson_detail, name='lesson_detail'), # 某视频课的详细信息
    path('lessons/<int:pk>/exercises/', exercises_list, name='exercises'), # 某视频课的所有练习
]