from django.db import models

from easymath.easymathbase_class import EasyMathBase


class Profile(EasyMathBase):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='用户')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='头像')
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class LearningPlan(EasyMathBase):
    title = models.CharField(max_length=120, verbose_name='学习计划名称')
    description = models.TextField(null=True, blank=True, verbose_name='学习计划描述')
    thumbnail = models.ImageField(null=True, blank=True, verbose_name='封面图片')
    is_public = models.BooleanField(default=False, verbose_name='公开')

    class Meta:
        verbose_name = '学习计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class LearningLog(EasyMathBase):
    slug = models.SlugField()

    class Meta:
        verbose_name = '学习日志'
        verbose_name_plural = verbose_name
