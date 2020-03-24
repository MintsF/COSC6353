from django.db import models

# Create your models here.
class UserInfo(models.Model):
	username = models.CharField(max_length=8,unique=True)
	password = models.CharField(max_length=256,null=False, blank = False)
	flag = models.IntegerField(null=False,default ='0')

class Profile(models.Model):
	username= models.OneToOneField(UserInfo, on_delete=models.CASCADE,unique=True)
	fullname= models.CharField(max_length=50, null =False, blank= False)
	address1 =models.CharField(max_length=100, null =False, blank= False)
	address2= models.CharField(max_length=100, null = True)
	city = models.CharField(max_length=100,null =False, blank= False)
	state = models.CharField(max_length=2,null= False, blank= False)
	zipcode = models.CharField(max_length=9, null= False, blank= False)

# class Order(models.Model):
# 	username = models.ForeignKey(to="UserInfo",to_field="username")
# 	deliveryDate= models.DateTimeField() 
# 	deliveryAddress = 
# 	deliveryCity= 
# 	deliveryState= 
# 	deliveryZipcode=
# 	gallons=
# 	amount=
	
	


		



