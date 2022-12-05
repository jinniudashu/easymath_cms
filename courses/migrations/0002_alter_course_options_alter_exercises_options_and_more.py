# Generated by Django 4.1.3 on 2022-12-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程', 'verbose_name_plural': '课程'},
        ),
        migrations.AlterModelOptions(
            name='exercises',
            options={'verbose_name': '习题', 'verbose_name_plural': '习题'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '视频', 'verbose_name_plural': '视频'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='allowed_memberships',
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='课程描述'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=120, verbose_name='课程名称'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='视频描述'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=120, verbose_name='视频名称'),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='单元名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='单元描述')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': '单元',
                'verbose_name_plural': '单元',
            },
        ),
        migrations.AlterField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.unit'),
        ),
        migrations.DeleteModel(
            name='Units',
        ),
    ]
