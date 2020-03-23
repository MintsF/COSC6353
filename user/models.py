from django.db import models

# Create your models here.
class UserInfo(models.Model):
	username = models.CharField(max_length=8,unique=True)
	password = models.CharField(max_length=256,null=False, blank = False)
	flag = models.IntegerField(null=False,default ='0')

class Profile(models.Model):
	fullname= models.CharField(max_length=256, null =False, blank= False)
	address1 =models.CharField(max_length=256, null =False, blank= False)
	address2= models.CharField(max_length=256)
	city = models.CharField(mar_length=2)
	state = models.CharField(mar_length=2,null= False, blank= False)



