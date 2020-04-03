from django.test import TestCase

# Create your tests here.
from user.models import UserInfo
from user.models import Order
from django.test import Client
from user import views
import json
from user.models import Profile

class UserInfoModelTest(TestCase):
	def setUp(self):

		UserInfo.objects.create(username= '11223344', password=123)

	def testUserInfoModel(self):
		result = UserInfo.objects.get(username=11223344)
		self.assertEqual(result.password,'123')

	def testLoginUrl(self):
		c=Client()
		response=c.post('/api/login/',{"username":"11223344","password":"123"})
		self.assertEqual(response.status_code,200)


	def testUserLogin(self):
		c=Client()
		response=c.post('/api/login/',{"username":"11223344","password":"123"})
		self.assertEqual(json.loads(response.content.decode())['code'],1002)

	def testUserLoginPasswordError(self):
		c=Client()
		response=c.post('/api/login/',{"username":"11223344","password":"122"})
		self.assertEqual(json.loads(response.content.decode())['code'],1001)

	def testUserLoginUsernameNotExit(self):

		c=Client()
		response=c.post('/api/login/',{"username":"","password":"122"})
		self.assertEqual(json.loads(response.content.decode())['code'],1001)

	def tearDown(self):
		print("user login model test finished")	

class RegisterModelTest(TestCase):
	def setUp(self):
		UserInfo.objects.create(username='11223344',password='123')

	def testRegisterUrl(self):
		c=Client()
		response= c.post('/api/register/',{"username":"11223344","password":"123"})
		self.assertEqual(response.status_code,200)


	def testUserRegister(self):
		c=Client()
		response=c.post('/api/register/', {"username": "11223355","password":"123"})
		self.assertEqual(json.loads(response.content.decode())['username'],"11223355")
		self.assertEqual(json.loads(response.content.decode())['password'],'123')
		self.assertEqual(json.loads(response.content.decode())['code'],2001)

	def testUsernameExist(self):
		c=Client()
		response=c.post('/api/register/',{"username":"11223344","password": "124"})
		self.assertEqual(json.loads(response.content.decode())['code'],2002)

	def tearDown(self):
		print("register model test finished")	

class ProfileModelTest(TestCase):
	def setUp(self):
		Profile.objects.create(username='11223344',fullname='Mike',address1='North Stadium', address2='',city='Houston', state='TX',zipcode='77700')
		UserInfo.objects.create(username= '11223344', password="123")

	def testProfileUrl(self):
		c=Client()
		response= c.post('/api/profile/',{"userid":"11223355","username":"Mike","address1":"North Stadium", "address2":"3333","city":"Houston", "state":"TX","zipcode":"77700"})
		self.assertEqual(response.status_code,200)

	def testProfileInsert(self):
		c= Client()
		response=c.post('/api/profile/',{"userid":"11223355","username":"Mike","address1":"North Stadium", "address2":"3333","city":"Houston", "state":"TX","zipcode":"77700"})
		self.assertEqual(json.loads(response.content.decode())['code'],3001)
		self.assertEqual(json.loads(response.content.decode())['username'],"Mike")
		self.assertEqual(json.loads(response.content.decode())['address1'],"North Stadium")
		self.assertEqual(json.loads(response.content.decode())['address2'],"3333")
		self.assertEqual(json.loads(response.content.decode())['city'],"Houston")
		self.assertEqual(json.loads(response.content.decode())['state'],"TX")
		self.assertEqual(json.loads(response.content.decode())['zipcode'],"77700")

	def testProfileUpdate(self):
		c=Client()
		response = c.post('/api/profile/',{"userid":"\"11223344\"","username":"Joe","address1":"North Stadium1", "address2":"4444","city":"Austin", "state":"CA","zipcode":"777009999"})
		self.assertEqual(json.loads(response.content.decode())['address2'],"4444")
		self.assertEqual(json.loads(response.content.decode())['code'],3002)
		self.assertEqual(json.loads(response.content.decode())['address1'],"North Stadium1")
		self.assertEqual(json.loads(response.content.decode())['city'],"Austin")
		self.assertEqual(json.loads(response.content.decode())['state'],"CA")
		self.assertEqual(json.loads(response.content.decode())['zipcode'],"777009999")
		self.assertEqual(json.loads(response.content.decode())['username'],"Joe")
		self.assertEqual(json.loads(response.content.decode())['userid'],"11223344")


	def testInitProfie(self):
		c=Client()
		UserInfo.objects.create(username= '11223366', password="123")
		response=c.post('/api/login/',{"username":"11223366","password":"123"})
		self.assertEqual(json.loads(response.content.decode())['flag'],0)
		response=c.post('/api/initProfile/',{"userid":"\"11223366\""})
		self.assertEqual(json.loads(response.content.decode())['code'],5003)

	def testChangePasswordUrl(self):
		c=Client()
		response= c.post('/api/changepassword/',{"username":"\"11223344\"","password":"123","newPassword":"134"})
		self.assertEqual(response.status_code,200)

	def testChangPassword(self):
		c=Client()
		response=c.post('/api/changepassword/',{"username":"\"11223344\"","password":"123","newPassword":"134"})
		self.assertEqual(json.loads(response.content.decode())['code'],4002)
		self.assertEqual(json.loads(response.content.decode())['password'],"134")

	def testChangePasswordOldPasswordError(self):
		c=Client()
		response= c.post('/api/changepassword/',{"username":"\"11223344\"","password":"124","newPassword":"134"})
		self.assertEqual(json.loads(response.content.decode())['code'],4001)

	def tearDown(self):
		print("profile model test finished")	


class FuelQuoteModelTest(TestCase):
	def setUp(self):
		UserInfo.objects.create(username='11223344', password='123',flag=1)
		Profile.objects.create(username='11223344', fullname='tom', address1='test address1',address2='test address2',city='test city',state='CA',zipcode='33333')
	
	def testGetUserProfileUrl(self):
		c=Client()
		response= c.post('/api/getUserProfile/',{"username":"11223344"})
		self.assertEqual(response.status_code,200)
	
	def testGetUserProfile(self):
		c=Client()
		# UserInfo.objects.create(username= '11223344', password="123")
		response=c.post('/api/login/',{"username":"11223344","password":"123"})
		self.assertEqual(json.loads(response.content.decode())['flag'],1)
		response=c.post('/api/getUserProfile/',{"username":"\"11223344\""})
		self.assertEqual(json.loads(response.content.decode())['code'],3001)

	def testGetUserProfileUrl(self):
		c=Client()
		response= c.post('/api/submitOrder/',{"username":"11223344"})
		self.assertEqual(response.status_code,200)

	def testSubmitOrder(self):
		c= Client()
		# response=c.post('/api/submitOrder/',{"username":"11223355","fullname":"Mike","address1":"North Stadium", "address2":"3333","city":"Houston", "state":"TX","zipcode":"77700"})
		response=c.post('/api/submitOrder/',{"username":"11223355","gallonsRequested":5,"deliveryAddress":"North Stadium", "deliveryDate":"2020-04-03 00:00:00","suggestedPrice":0.5, "totalAmountDue":10.6})
		# newOrder=Order.objects.create(username=username,gallonsRequested=gallonsRequested,deliveryAddress=deliveryAddress,deliveryDate=deliveryDate,suggestedPrice=suggestedPrice,totalAmountDue=totalAmountDue)
		self.assertEqual(json.loads(response.content.decode())['code'],2001)
		self.assertEqual(json.loads(response.content.decode())['username'],"11223355")
		self.assertEqual(json.loads(response.content.decode())['gallonsRequested'],"5")
		self.assertEqual(json.loads(response.content.decode())['deliveryAddress'],"North Stadium")
		self.assertEqual(json.loads(response.content.decode())['deliveryDate'],"2020-04-03 00:00:00")
		self.assertEqual(json.loads(response.content.decode())['suggestedPrice'],"0.5")
		self.assertEqual(json.loads(response.content.decode())['totalAmountDue'],"10.6")

	# 	act = {}
	def tearDown(self):
		print("fuel quote model test finished")

class tetGetOrderHistory(TestCase):
	def setUp(self):
		UserInfo.objects.create(username='11223344', password='123',flag=1)
		Profile.objects.create(username='11223344', fullname='tom', address1='test address1',address2='test address2',city='test city',state='TX',zipcode='00111')
		Order.objects.create(username='11223344',gallonsRequested=5,deliveryAddress='deliveryAddress',deliveryDate='2020-04-03 00:00:00',suggestedPrice=0.5,totalAmountDue=1.5)
	
	def testGetOrderHistoryUrl(self):
		c=Client()
		response= c.post('/api/getOrderHistory/',{"username":"11223344"})
		self.assertEqual(response.status_code,200)    
	
	def testGetOrderHistory(self):
		c=Client()
		# UserInfo.objects.create(username= '11223344', password='123')
		response=c.post('/api/login/',{"username":"11223344","password":"123"})
		self.assertEqual(json.loads(response.content.decode())['flag'],1)
		response=c.post('/api/getOrderHistory/',{"username":"11223344"})
		self.assertEqual(json.loads(response.content.decode())['code'],4001)

	def tearDown(self):
		print("fuel order history model test finished")	





		







