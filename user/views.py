from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

# Create your views here.
def login(request):
	pass
	return render(request,'login/login.html')
# class RegisterView(APIView):
# 	def post(self, request, *args, **kwargs):
# 		ret= {'code':1000, 'msg':None}
# 		try:
# 			username= request._request.POST.get('username')
# 			password = request._request.POST.get('password')
# 			obj = models.UserInfo.objects.create(username=username,password=password)
# 			if not obj:
# 				models.UserInfo.objects.create(username=username,password= password)
# 				ret['code']=100
# 				ret['msg']= u'create success'
# 			else:
# 				ret['code']=101
# 				ret['msg']= u'user existed'
# 		except Exception as e:
# 			ret['code'] =102
# 			ret['msg']= u'register front-end submit/db rw error '
# 		return JsonResponse(ret)


# class LoginView(APIView):
# 	def post(self,request,*args, **kwargs):
# 		ret ={'code': 1000, 'msg': None}
# 		try:
# 			username =username= request._request.POST.get('username')
# 			password = request._request.POST.get('password')
# 			obj = models.UserInfo.objects.create(username=username,password=password)
# 			if not obj:
# 				ret['code']=1001
# 				ret['msg'] ='user name or password error'
# 		except Exception as e:
# 			ret['code']=1002
# 			ret['msg']= 'login  front-end submit/db rw error '

# 		return JsonResponse(ret)

