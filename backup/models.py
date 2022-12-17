from django.db import models

# 备份模型抽象类
class Backup(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, verbose_name="版本")
    label = models.CharField(max_length=255, null=True, blank=True, verbose_name="版本名称")
    code = models.TextField(null=True, verbose_name="数据脚本")
    description = models.TextField(max_length=255, verbose_name="描述", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  

    class Meta:
        verbose_name = "数据备份"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.create_time)

