from django.db import models

class user_info1(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=16)
    ugender = models.BooleanField()
    ueamil = models.CharField(max_length=20)
    utell = models.CharField(max_length=11)
    uaddress = models.CharField(max_length=40)
    isDelete = models.BooleanField()
    def __unicode__(self):
        return self.pk
