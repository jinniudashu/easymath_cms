from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, Unit, Lesson, Exercise


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

@api_view(['GET'])
def courses_list(request):
    courses_list = Course.objects.all()
    serializer = CourseSerializer(courses_list, many=True)
    return Response(serializer.data)


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

@api_view(['GET'])
def units_list(request):
    units_list = Unit.objects.all()
    serializer = UnitSerializer(units_list, many=True)
    return Response(serializer.data)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

@api_view(['GET'])
def lessons_list(request):
    lessons_list = Lesson.objects.all()
    serializer = LessonSerializer(lessons_list, many=True)
    return Response(serializer.data)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

@api_view(['GET'])
def exercises_list(request):
    exercises_list = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises_list, many=True)
    return Response(serializer.data)