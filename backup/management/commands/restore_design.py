from django.core.management import BaseCommand
import json

from courses.models import *
from learning_management.models import *
from memberships.models import *
from backup.admin import Backup_models


class Command(BaseCommand):
    help = 'Restore design data from backuped json file'

    def handle(self, *args, **options):
        make_sure = input('''如果当前是在生产系统上操作，请确认数据是最新版本的备份！\n是否要开始恢复数据操作？(y/n)''')
        if make_sure != 'y':
            print('Cancel restore data...')
            return
        else:
            print('start restore data...')

        # 读取备份数据文件
        backuped_json_file = 'backup/data_backup.json'
        with open(backuped_json_file, encoding="utf8") as f:
            design_data = json.loads(f.read())


        for model in Backup_models:
            print(model._meta.model_name)
            result = model.objects.restore_data(design_data[model._meta.model_name])
            print(result)
        
        print('恢复设计数据完成！')
