from django.db import models

# Create your models here.
class UserInfo(models.Model):
	username = models.CharField(max_length=8,unique=True)
	password = models.CharField(max_length=256,null=False, blank = False)
	flag = models.IntegerField(null=False,default ='0')

