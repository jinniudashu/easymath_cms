from django.db import models
from django.forms.models import model_to_dict
from datetime import timedelta
import uuid
import re


# 自定义管理器：设计数据备份、恢复
class EasyMathBackupManager(models.Manager):
    def backup_data(self, queryset=None):
        backup_data = []
        
        if queryset is None:
            queryset = self.all()
            
        for item in queryset:
            item_dict = model_to_dict(item)

            # 遍历模型非多对多字段，如果是外键，则用外键的easymath_id替换外键id
            for field in self.model._meta.fields:
                # if item_dict[field.name] or field.__class__.__name__ == 'DurationField':  # 如果字段不为空或字段为DurationField类型，进行检查替换
                if item_dict[field.name]:  # 如果字段不为空或字段为DurationField类型，进行检查替换
                    if (field.one_to_one or field.many_to_one):  # 一对一、多对一字段, 获取外键的easymath_id
                        _object = field.related_model.objects.get(id=item_dict[field.name])
                        item_dict[field.name] = _object.easymath_id
                    elif field.__class__.__name__ == 'DurationField':  # duration字段
                        item_dict[field.name] = str(item_dict[field.name])
                    elif field.__class__.__name__ == 'CloudinaryField':
                        item_dict[field.name] = str(item_dict[field.name])


            # 遍历模型多对多字段，用easymath_id替换外键id
            for field in self.model._meta.many_to_many:
                if item_dict[field.name]:  # 如果字段不为空，进行检查替换
                    # 先获取多对多字段对象的id List
                    _ids = []
                    for _field in item_dict[field.name]:
                        _ids.append(_field.id)
                    ids = []
                    for _object in field.related_model.objects.filter(id__in=_ids):
                        ids.append(_object.easymath_id)
                    item_dict[field.name] = ids

            item_dict.pop('id')  # 删除id字段
            backup_data.append(item_dict)

        return backup_data


    def restore_data(self, data):
        print('开始恢复：', self.model.__name__)
        self.all().delete()

        if data is None or len(data) == 0:
            return 'No data to restore'

        for item_dict in data:
            item = {}
            # 遍历模型非多对多字段，如果是外键，则用外键的easymath_id找回关联对象
            for field in self.model._meta.fields:
                if item_dict.get(field.name) is not None:  # 如果字段不为空，进行检查替换                    
                    if (field.one_to_one or field.many_to_one):  # 一对一、多对一字段, 用easymath_id获取对象
                        try:
                            _object = field.related_model.objects.get(easymath_id=item_dict[field.name])
                        except field.related_model.DoesNotExist:
                            _object = None

                        item[field.name] = _object

                    elif field.__class__.__name__ == 'DurationField':  # duration字段
                        item[field.name] = self._parse_timedelta(item_dict[field.name])

                    elif field.__class__.__name__ == 'CloudinaryField':
                        print('CloudinaryField', item_dict[field.name])

                    else:
                        item[field.name] = item_dict[field.name]


            # 插入构造好的记录，不包括多对多字段
            _instance=self.model.objects.create(**item)


            # 遍历模型多对多字段，用easymath_id获取对象
            for field in self.model._meta.many_to_many:
                if item_dict.get(field.name):  # 如果字段不为空，进行检查替换
                    objects = []
                    for _object in field.related_model.objects.filter(easymath_id__in=item_dict[field.name]):
                        objects.append(_object)

                    # 将对象添加到多对多字段中
                    eval(f'_instance.{field.name}').set(objects)
            
        return f'{self.model} 已恢复'


    @staticmethod
    def _parse_timedelta(stamp):
    # 转换string to timedelta
        if 'day' in stamp:
            m = re.match(r'(?P<d>[-\d]+) day[s]*, (?P<h>\d+):'
                        r'(?P<m>\d+):(?P<s>\d[\.\d+]*)', stamp)
        else:
            m = re.match(r'(?P<h>\d+):(?P<m>\d+):'
                        r'(?P<s>\d[\.\d+]*)', stamp)
        if not m:
            return ''

        time_dict = {key: float(val) for key, val in m.groupdict().items()}
        if 'd' in time_dict:
            return timedelta(days=time_dict['d'], hours=time_dict['h'],
                            minutes=time_dict['m'], seconds=time_dict['s'])
        else:
            return timedelta(hours=time_dict['h'],
                            minutes=time_dict['m'], seconds=time_dict['s'])


# EasyMath基类
class EasyMathBase(models.Model):
    easymath_id = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="EasyMathID")
    objects = EasyMathBackupManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.easymath_id is None:
            self.easymath_id = uuid.uuid1()
        super().save(*args, **kwargs)
