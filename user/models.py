from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)

    def __str__(self):
        return '用户名%s' % self.username
