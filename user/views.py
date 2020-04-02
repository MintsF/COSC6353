# from django.shortcuts import render
# from rest_framework.views import APIView
# from django.http import JsonResponse
# # from rest_framework.decorators import api_view
# class RegisterView(APIView):
# 	# @api_view(['POST'])
# 	def post(self, request,*args,**kwargs):
# 		ret= {'code':1000, 'msg':None}
		
# 		try:
# 			username= request.POST.get('username',None)
# 			password = request.POST.get('password',None)
# 			# username= request._request.POST.get('username',None)
# 			# password = request._request.POST.get('password',None)
# 			obj = models.UserInfo.objects.create(username=username,password=password)
# 			if not obj:
# 				newUser=models.UserInfo.objects.create(username=username,password= password)
# 				newUser.save()
# 				ret['code']=100
# 				ret['msg']= u'create account success'
# 				print(request.body)
# 				print(request.POST)
# 			else:
# 				ret['code']=101
# 				ret['msg']= u'user existed'
# 		except Exception as e:
# 			ret['code'] =102
# 			ret['msg']= u'register front-end submit/db rw error '
# 		return JsonResponse(ret)



# class LoginView(APIView):
# 	# @api_view(['GET'])
# 	def get(self,request,*args,**kwargs):
		
# 		ret ={'code': 1000, 'msg': None}
# 		try:

# 			# print(request.body)
# 				# username = request.data.get('username',None)
# 			# password = request.data.get('password')
# 			# print(username)
# 			# # obj = auth.authenticate(request,username=user, password = password)
# 			# obj = models.UserInfo.objects.create(username=username,password=password)
# 			# if not obj:
# 			# 	ret['code']=1001
# 			# 	ret['msg'] ='user name or password error'
# 			# else:
# 				queryset = UserInfo.objects.all()
# 				print(queryset)
# 				ret['code'] =1000
# 				ret['msg']='user login success'

# 		except Exception as e:
# 			ret['code']=1002
# 			ret['msg']= 'login  front-end submit/db rw error '

# 		print(request.body)
# 		print(request.POST)

# 		return JsonResponse(ret)



from django.shortcuts import render
from django.http import JsonResponse
# from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# from django.core import serializers
from .models import UserInfo,Profile,Order

# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json



# @require_http_methods(['POST'])
# @csrf_exempt
# @require_http_methods(['GET'])
# @require_http_methods(['POST'])
@api_view(['POST'])
def show_info(request):
  response = {'code': 1000, 'username':None, 'password': None,'msg': None}
  try:
    
    # request_data=json.loads(request.body)
    print(request.user)
    print(request.body)



    username = request.POST.get("username",1)
   
    password = request.POST.get("password",1)
    # obj=models.UserInfo.objects.get('data')

    response['username']= username
    response['password']=password

    response['msg'] = 'success'
    response['error_num'] = 0
  except Exception as e:
    response['msg'] = str(e)
    response['error_num'] = 1
  return JsonResponse(response)



@api_view(['POST'])
def login(request):
	ret ={'code': 1000, 'username':None, 'password': None, 'flag':None,'msg': None}
	try:
		username = request.POST.get('username')
		password = request.POST.get('password')
		obj = UserInfo.objects.filter(username=username,password=password).count()
		if obj==0:
			ret['code']= 1001
			ret['msg']='username or password error'
		else:
			ret['code']=1002
			ret['username']=username
			ret['password']=password
			ret['flag']=UserInfo.objects.get(username=username,password=password).flag
			ret['msg']= username+' login success'


	except Exception as e:
		ret['code'] = 1003
		ret['msg'] = 'can not connect to front end'
	return JsonResponse(ret)

@api_view(['POST'])
def register(request):
	ret ={'code': 2000, 'username':None, 'password': None, 'flag':None,'msg': None}
	try:
		username= request.POST.get('username')
		password = request. POST.get('password')
		# print(username)
		obj = UserInfo.objects.filter(username=username).count()

		if obj==0:
			newUser=UserInfo.objects.create(username=username,password=password,flag=0)
			newUser.save()
			ret['code']=2001
			ret['flag']=0
			ret['username']=username
			ret['password']=password
			ret['msg']= username+ ' register success'
		else:
			ret['code']=2002
			ret['msg']= 'username existed'


	except Exception as e:
		ret['code']= 2005
		ret['msg']='can not connect to front end'
	return JsonResponse(ret)


@api_view(['POST'])
def getUserProfile(request):
	ret = {'code': 3000, 'profile': None}
	# try:
	username = request.POST.get('username')
	print(username)
	# check whether exist this user
	obj = Profile.objects.filter( fullname = username)
	print(obj)
	if obj.count() == 0:
		# test, database have no data
		ret['profile']={
			'address1' : 'no address',
			'address2':'',
			'city':'Houston',
			'state':'TX',
			'zipCode':'77077'
		}
	else:
		ret['profile'] = {
			'address1': obj.address,
			'address2': '',
			'city': obj.city,
			'state': obj.status,
			'zipCode': obj.zipCode
		}
	# except Exception as e:
	# 	ret['code'] = 2005
	# 	ret['msg'] = 'can not connect to front end'
	return JsonResponse(ret)

@api_view(['POST'])
def profile(request):
	ret ={'code': 2000, 'username':None, 'flag':None,'msg': None, 'userid': None, 'address1': None, 'address2': None, 'city': None, 'state':None, 'zipcode': None}
	try:
		username= request.POST.get('username')
		print(username)
		# fullname= request.POST.get('fullname')
		# password = request. POST.get('password')
		address1 = request. POST.get('address1')
		address2 = request. POST.get('address2')
		city = request. POST.get('city')
		state = request. POST.get('state')
		zipcode = request. POST.get('zipcode')
		print('Hi, before executed Profile class')
		obj = Profile.objects.filter(username=username).count()
		print('Hi')
		if obj==0:
			newUser=Profile.objects.create(username=username,address1=address1,address2=address2,city=city,state=state,zipcode=zipcode)
			newUser.save()
			ret['username']=username
			# ret['fullname']=fullname
			ret['address1']=address1
			ret['address2']=address2
			ret['city']=city
			ret['state']=state
			ret['zipcode']=zipcode
			ret['msg']= username+ ' profiles was successfully conducted'
		else:
			ret['code']=2002
			ret['msg']= 'username existed'
	except Exception as e:
		ret['code'] = 2005
		ret['msg'] = 'can not connect to front end'	
	return JsonResponse(ret)
	
@api_view(['POST'])
def submitOrder(request):
	ret ={'code': 2000, 'username':None,  'gallonsRequested':None, 'deliveryAddress': None,'deliverDate': None,'suggestedPrice':None, 'totalAmountDue':None}
	# try:
	username= request.POST.get('username')
	gallonsRequested = request.POST.get('gallonsRequested')
	deliveryAddress = request.POST.get('deliveryAddress')
	deliveryDate = request.POST.get('deliveryDate')
	print(deliveryDate)
	suggestedPrice = request.POST.get('suggestedPrice')
	totalAmountDue = request.POST.get('totalAmountDue')

	print(username)
	newOrder=Order.objects.create(username=username,gallonsRequested=gallonsRequested,deliveryAddress=deliveryAddress,deliveryDate=deliveryDate,suggestedPrice=suggestedPrice,totalAmountDue=totalAmountDue)
	newOrder.save()


	# except Exception as e:
	# 	ret['code']= 2005
	# 	ret['msg']='can not connect to front end'
	return JsonResponse(ret)

@api_view(['POST'])
def getOrderHistory(request):
	ret ={'code': 2000, 'total':None,'orderList':[],}
	# try:
	username= request.POST.get('username')
	print(username)
	obj = Order.objects.filter(username = username)
	# print(obj.values())
	# print(obj.count())
	ret['total'] = obj.count()
	if(obj.count() == 0):
		ret['orderList'] = {
			'gallonsRequested': 0,
			'deliveryAddress':"00",
			'deliveryDate': "00",
			'suggestedPrice': 0,
			'totalAmountDue': 0
		}
	else:
		i=0
		for order in obj:
			print(order)
			i=i+1
			print(i)
			ret['orderList'].append({
				'gallonsRequested': order.gallonsRequested,
				'deliveryAddress': order.deliveryAddress,
				'deliveryDate': order.deliveryDate,
				'suggestedPrice': order.suggestedPrice,
				'totalAmountDue': order.totalAmountDue
			})


	# except Exception as e:
	# 	ret['code']= 2005
	# 	ret['msg']='can not connect to front end'
	return JsonResponse(ret)
