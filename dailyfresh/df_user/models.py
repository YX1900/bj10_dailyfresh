# coding=utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    '''
    用户模型类
    '''
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    email = models.EmailField()