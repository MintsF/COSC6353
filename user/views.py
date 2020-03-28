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
from .models import UserInfo,Profile
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


@api_view(['GET'])
def getUserProfile(request):
	ret = {'code': 3000, 'profile': None}
	try:
		username = request.POST.get('username')
		# print(username)
		# check whether exist this user
		obj = Profile.objects.filter(username=username).count()
		print(obj)
		if obj == 0:
			# test, database have no data
			ret['profile']={
				'address' : 'test address',
				'city':'Houston',
				'state':'TX',
				'zipCode':'77077'
			}
		else:
			ret['profile'] = {
				'address': 'test address',
				'city': 'Houston',
				'state': 'TX',
				'zipCode': '77077'
			}
	except Exception as e:
		ret['code'] = 2005
		ret['msg'] = 'can not connect to front end'
	return JsonResponse(ret)



