from django.db import models
from django.urls import reverse

from cloudinary.models import CloudinaryField


# 系列课
class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120, verbose_name='课程名称')
    description = models.TextField(null=True, blank=True, verbose_name='课程描述')
    thumbnail = CloudinaryField('thumbnail', null=True, blank=True)
    
    class Meta:
        verbose_name = '系列课'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'slug': self.slug})

    @property
    def units(self):
        return self.unit_set.all().order_by('position')

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


# 课程单元
class Unit(models.Model):
    position = models.IntegerField(default=10, verbose_name='单元顺序')
    title = models.CharField(max_length=120, verbose_name='单元名称')
    description = models.TextField(null=True, blank=True, verbose_name='单元描述')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  verbose_name='所属课程')

    class Meta:
        verbose_name = '课程单元'
        verbose_name_plural = verbose_name
        ordering = ['course', 'position']

    def __str__(self):
        return self.title

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

# 视频课
class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120, verbose_name='视频名称')
    description = models.TextField(null=True, blank=True, verbose_name='视频描述')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, verbose_name='所属课程')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='单元')
    position = models.IntegerField(default=10, verbose_name='视频顺序')
    video = CloudinaryField('video', null=True, blank=True)
    video_additional = CloudinaryField('video_additional', null=True, blank=True)
    thumbnail = CloudinaryField('thumbnail', null=True, blank=True)
    is_free = models.BooleanField(default=False, verbose_name='免费试看')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        ordering = ['course', 'unit', 'position']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson-detail', kwargs={'course_slug': self.course.slug, 'lesson_slug': self.slug})


# 习题
class Exercise(models.Model):
    position = models.IntegerField(default=10, verbose_name='习题顺序')
    title = models.CharField(max_length=120, verbose_name='习题名称')
    question = models.TextField(verbose_name='习题描述')
    answer = models.CharField(max_length=120, verbose_name='答案')
    question_image = CloudinaryField('question_image', null=True, blank=True)
    answer_image = CloudinaryField('answer_image', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='所属视频')

    class Meta:
        verbose_name = '习题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
