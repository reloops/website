# Generated by Django 3.2.2 on 2021-05-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_pastline_createtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Futureline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('detail', models.CharField(max_length=100, verbose_name='详细')),
                ('targettime', models.CharField(max_length=20, verbose_name='计划时间')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]