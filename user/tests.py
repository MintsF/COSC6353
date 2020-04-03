from django.test import TestCase

# Create your tests here.
from user.models import UserInfo
from django.test import Client
from user import views
import json


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

class FuelQuoteModelTest(TestCase):
	def setUp(self):
		# UserInfo.objects.create(username='11223344',password='123')
	    Activity.objects.create(id=1, username='11223344', fullname='tom', address1='test address1',address2='test address2',city='test city',state='test state',zipcode='test zipcode')
	
	def testGetUserProfileUrl(self):
		c=Client()
		response= c.post('/api/getUserProfile/',{"username":"11223344"})
		self.assertEqual(response.status_code,200)
	
	def testGetUserProfile(self):
		A = profile()
		post = A.post()
		self.assertEqual(len(post),1)

	# def testSubmitOrder(self):
	# 	act = {}
    # def tearDown(self):


                  






		







