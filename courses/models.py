from django.db import models
from django.urls import reverse


# 获取上传文件的路径
def upload_location(instance, filename):
    if isinstance(instance, Course):
        return f'test/{instance.title}/{filename}'
    elif isinstance(instance, Lesson):
        return f'test/{instance.course.title}/{instance.title}/{filename}'
    elif isinstance(instance, Exercises):
        return f'test/{instance.lesson.course.title}/{instance.lesson.title}/{instance.title}/{filename}'


# 系列课
class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120, verbose_name='课程名称')
    description = models.TextField(null=True, blank=True, verbose_name='课程描述')
    thumbnail = models.FileField(upload_to=upload_location, null=True, blank=True, verbose_name='封面图片')
    # thumbnail = models.FileField(upload_to='test/', null=True, blank=True, verbose_name='封面图片')
    
    class Meta:
        verbose_name = '系列课'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'slug': self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


# 课程单元
class Unit(models.Model):
    position = models.IntegerField(default=10, verbose_name='单元顺序')
    title = models.CharField(max_length=120, verbose_name='单元名称')
    description = models.TextField(null=True, blank=True, verbose_name='单元描述')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程单元'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 视频课
class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120, verbose_name='视频名称')
    description = models.TextField(null=True, blank=True, verbose_name='视频描述')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='所属课程')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='单元')
    position = models.IntegerField(default=10, verbose_name='视频顺序')
    video = models.FileField(upload_to=upload_location, null=True, blank=True, verbose_name='视频')
    thumbnail = models.FileField(upload_to=upload_location, null=True, blank=True, verbose_name='封面图片')
    # video = models.FileField(upload_to='test/', null=True, blank=True, verbose_name='视频')
    # thumbnail = models.FileField(upload_to='test/', null=True, blank=True, verbose_name='封面图片')
    is_free = models.BooleanField(default=False, verbose_name='免费试看')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson-detail', kwargs={'course_slug': self.course.slug, 'lesson_slug': self.slug})


# 习题
class Exercises(models.Model):
    position = models.IntegerField(default=10, verbose_name='习题顺序')
    title = models.CharField(max_length=120, verbose_name='习题名称')
    question = models.TextField(verbose_name='习题描述')
    answer = models.CharField(max_length=120, verbose_name='答案')
    question_image = models.FileField(upload_to=upload_location, null=True, blank=True, verbose_name='习题图片')
    answer_image = models.FileField(upload_to=upload_location, null=True, blank=True, verbose_name='答案图片')
    # question_image = models.FileField(upload_to='test/', null=True, blank=True, verbose_name='习题图片')
    # answer_image = models.FileField(upload_to='test/', null=True, blank=True, verbose_name='答案图片')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='所属视频')

    class Meta:
        verbose_name = '习题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
