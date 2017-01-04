from django.db import models

# Create your models here.
class goodslist(models.Model):
	goods_name = models.CharField(max_length=100)
	goods_type = models.CharField(max_length=100)
	goods_price = models.FloatField()
	goods_descriptions = models.TextField()
	goods_delete = models.BooleanField()
	goods_fk = models.ForeignKey('typeinfo')

	def __str__(self):
		return self.pk

class typeinfo(models.Model):
	type_name = models.CharField(max_length=100)
	type_delete = models.BooleanField()

	def __str__(self):
		return self.pk