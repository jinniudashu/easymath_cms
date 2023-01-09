from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, Unit, Lesson, Exercise


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


# 去除thumbnail字段开头的‘image/upload/’前缀
def remove_thumbnail_prefix(serializer_data):
    for i in range(len(serializer_data)):
        if serializer_data[i]['thumbnail']:
            serializer_data[i]['thumbnail'] = serializer_data[i]['thumbnail'][13:]
    return serializer_data


@api_view(['GET'])
def courses_list(request):
    '''所有系列课'''
    courses_list = Course.objects.all()
    serializer = CourseSerializer(courses_list, many=True)

    # thumbnail序列化值去掉开头的‘image/upload/’
    serializer_data = remove_thumbnail_prefix(serializer.data)

    return Response(serializer_data)


@api_view(['GET'])
def units_list(request, pk):
    '''某系列课的所有单元'''
    units_list = Unit.objects.filter(course=pk)
    serializer = UnitSerializer(units_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lessons_list(request, pk):
    '''某系列课的所有视频课'''
    lessons_list = Lesson.objects.filter(course=pk)
    serializer = LessonSerializer(lessons_list, many=True)

    # thumbnail序列化值去掉开头的‘image/upload/’
    serializer_data = remove_thumbnail_prefix(serializer.data)

    return Response(serializer_data)


@api_view(['GET'])
def unit_lessons_list(request, cpk, upk):
    '''某系列课的某单元的所有视频课'''
    lessons_list = Lesson.objects.filter(course=cpk, unit=upk)
    serializer = LessonSerializer(lessons_list, many=True)

    # thumbnail序列化值去掉开头的‘image/upload/’
    serializer_data = remove_thumbnail_prefix(serializer.data)

    return Response(serializer_data)


@api_view(['GET'])
def lesson_detail(request, pk):
    '''某视频课的详细信息'''
    lesson = Lesson.objects.get(id=pk)
    serializer = LessonSerializer(lesson, many=False)

    # thumbnail序列化值去掉开头的‘image/upload/’
    serializer_data = remove_thumbnail_prefix([serializer.data])

    return Response(serializer_data[0])


@api_view(['GET'])
def exercises_list(request, pk):
    '''某视频课的所有练习'''
    exercises_list = Exercise.objects.filter(lesson=pk)
    serializer = ExerciseSerializer(exercises_list, many=True)
    return Response(serializer.data)