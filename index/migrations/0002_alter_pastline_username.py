# Generated by Django 3.2.2 on 2021-05-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastline',
            name='username',
            field=models.CharField(max_length=30, verbose_name='用户名'),
        ),
    ]
