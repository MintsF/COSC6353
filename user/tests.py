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

class ProfileModelTest(TestCase):
	def setUp(self):
		Profile.objects.create(username='11223344',fullname='Mike',address1='North Stadium', address2='',city='Houston', state='TX',zipcode='77700')
		UserInfo.objects.create(username= '11223344', password="123")

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

	def testChangPassword(self):
		c=Client()
		response=c.post('/api/changepassword/',{"username":"\"11223344\"","password":"123","newPassword":"134"})
		self.assertEqual(json.loads(response.content.decode())['code'],4002)
		self.assertEqual(json.loads(response.content.decode())['password'],"134")

	def testChangePasswordOldPasswordError(self):
		c=Client()
		response= c.post('/api/changepassword/',{"username":"\"11223344\"","password":"124","newPassword":"134"})
		self.assertEqual(json.loads(response.content.decode())['code'],4001)




# class FuelQuoteModelTest(TestCase):
class FuelQuoteModelTest(TestCase):
	def setUp(self):
		UserInfo.objects.create(username='11223344', password='123')
		Profile.objects.create(id=1, username='11223344', fullname='tom', address1='test address1',address2='test address2',city='test city',state='test state',zipcode='test zipcode')
	
	def testGetUserProfileUrl(self):
		c=Client()
		response= c.post('/api/getUserProfile/',{"username":"11223344"})
		self.assertEqual(response.status_code,200)
	
	def testGetUserProfile(self):
		c=Client()
		UserInfo.objects.create(username= '11223344', password="123")
		response=c.post('/api/login/',{"username":"11223344","password":"123"})
		self.assertEqual(json.loads(response.content.decode())['flag'],1)
		response=c.post('/api/getUserProfile/',{"userid":"\"11223344\""})
		self.assertEqual(json.loads(response.content.decode())['code'],3001)

	def testSubmitOrder(self):
		c= Client()
		response=c.post('/api/submitOrder/',{"username":"11223355","fullname":"Mike","address1":"North Stadium", "address2":"3333","city":"Houston", "state":"TX","zipcode":"77700"})
		# newOrder=Order.objects.create(username=username,gallonsRequested=gallonsRequested,deliveryAddress=deliveryAddress,deliveryDate=deliveryDate,suggestedPrice=suggestedPrice,totalAmountDue=totalAmountDue)
		self.assertEqual(json.loads(response.content.decode())['code'],2001)
		self.assertEqual(json.loads(response.content.decode())['username'],"Mike")
		self.assertEqual(json.loads(response.content.decode())['address1'],"North Stadium")
		self.assertEqual(json.loads(response.content.decode())['address2'],"3333")
		self.assertEqual(json.loads(response.content.decode())['city'],"Houston")
		self.assertEqual(json.loads(response.content.decode())['state'],"TX")
		self.assertEqual(json.loads(response.content.decode())['zipcode'],"77700")

	# 	act = {}
	def tearDown(self):
		print("fuel quote model test finished")


                  






		







