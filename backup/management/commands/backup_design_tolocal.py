from django.core.management import BaseCommand
import requests


class Command(BaseCommand):
    help = '导入系统数据，保存为本地JSON文件'

    def handle(self, *args, **kwargs):
        url = 'http://127.0.0.1:8000/backup/data_backup/'
        output_file = 'backup/data_backup.json'
        make_sure = input(f'''即将从{url}倒入设计备份数据到本地{output_file}，请确认导入来源！\n是否要开始？(y/n)''')
        if make_sure == 'y':

            print(f'从{url}导入设计数据备份...')
            res = requests.get(url)
            res_json = res.json()[0]
            code = res_json['code']

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(code)

            print(f'备份数据到{output_file}完成！')
        
        else:
            print('操作已取消！')