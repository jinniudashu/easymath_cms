from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
import json
from time import time

from courses.models import Course, Unit, Lesson, Exercises
from learning_management.models import *
from memberships.models import *
from .models import Backup

# 每个需要备份的model都需要在这里添加
# 不备份在其他表新增内容时自动插入内容的表，Component, RelateFieldModel
Backup_models = [
    Course,
    Unit,
    Lesson,
    Exercises,
    Membership,
    UserMembership,
    Subscription,
    Profile,
    LearningPlan,
    LearningLog,
]

@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')
    # 增加一个自定义按钮“备份数据”
    change_list_template = 'data_backup_changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('data_backup/', self.data_backup),
        ]
        return my_urls + urls

    # 备份数据
    def data_backup(self, request):
        design_data = {}
        for model in Backup_models:
            _model = model.__name__.lower()
            design_data[_model]=model.objects.backup_data()
            json.dumps(design_data[_model], indent=4, ensure_ascii=False, cls=DjangoJSONEncoder)
        
        backup_name = str(int(time()))
        # 写入数据库
        result = Backup.objects.create(
            name = backup_name,
            code = json.dumps(design_data, indent=4, ensure_ascii=False, cls=DjangoJSONEncoder),
        )
        print(f'数据备份成功, id: {result}')

        # 写入json文件
        print('开始写入json文件...')
        with open(f'./backup/backup_{backup_name}.json', 'w', encoding='utf-8') as f:
            json.dump(design_data, f, indent=4, ensure_ascii=False, cls=DjangoJSONEncoder)
            print(f'JSON写入成功, id: {backup_name}')

        return HttpResponseRedirect("../")

