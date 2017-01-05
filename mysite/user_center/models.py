#coding=utf8
from django.db import models
from user_info.models import *

# Create your models here.


class userCenter(models.Model):
    uc_name = models.CharField(max_length=10)
    uc_address = models.CharField(max_length=100)
    uc_phone = models.CharField(max_length=15)
    uc_zipcode = models.CharField(max_length=10)
    uc_isDelete = models.BooleanField(default=False)
    uc_user = models.ForeignKey('user_info.user_info1')