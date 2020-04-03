from django.conf.urls import url,include

from . import views


urlpatterns = [

    url(r'login/$',views.login,),
    url(r'register/$',views.register,),
    url(r'profile/$',views.profile,),
    url(r'getUserProfile/$',views.getUserProfile,),
    url(r'submitOrder/$',views.submitOrder),
    url(r'getOrderHistory/$',views.getOrderHistory),
    url(r'changepassword/$', views.changepassword,),
    url(r'initProfile/$',views.initprofile,),


	
]