# Generated by Django 4.1.3 on 2022-12-17 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_management', '0002_learninglog_easymath_id_learningplan_easymath_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learninglog',
            name='easymath_id',
        ),
        migrations.RemoveField(
            model_name='learningplan',
            name='easymath_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='easymath_id',
        ),
    ]
