from django.db import models

# Create your models here.
class user_info(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=16)
    ugender = models.BooleanField()
    utell = models.IntegerField(max_length=11)
    uaddress = models.CharField(max_length=40)
    isDelete = models.BooleanField()
    def __unicode__(self):
        return self.pk
