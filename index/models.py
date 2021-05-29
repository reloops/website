import time

from django.db import models


# Create your models here.
# from django.utils import timezone


class Pastline(models.Model):
    username = models.CharField("用户名", max_length=30)
    detail = models.CharField("详细", max_length=100, null=False)
    createtime = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return '用户名%s' % self.username


class Futureline(models.Model):
    username = models.CharField("用户名", max_length=30)
    detail = models.CharField("详细", max_length=100)
    targettime = models.CharField("计划时间", max_length=20)
    createtime = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return '用户名%s' % self.username
