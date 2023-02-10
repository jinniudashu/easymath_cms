from django.core.exceptions import ObjectDoesNotExist
from courses.models import Course, Lesson

import urllib.request
from PIL import Image

def resize_image(url, filename, size):
    image = Image.open(urllib.request.urlopen(url))
    image = image.resize(size, Image.ANTIALIAS)
    image.save(f'courses/batch_upload/images/{filename}.png', 'PNG')

def down_images():
    courses = Course.objects.all()
    for course in courses:
        try:
            url = course.thumbnail.url
            filename = course.thumbnail_name
            if filename:
                resize_image(url, filename, (400, 225))
        except ObjectDoesNotExist:
            print(course.title, '没有封面图片')

    lessons = Lesson.objects.all()
    for lesson in lessons:
        try:
            url = lesson.thumbnail.url
            filename = lesson.thumbnail_name
            if filename:
                resize_image(url, filename, (400, 225))
        except ObjectDoesNotExist:
            print(lesson.title, '没有封面图片')