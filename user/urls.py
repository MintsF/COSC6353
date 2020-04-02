from django.conf.urls import url,include

from . import views


urlpatterns = [
    # url(r'register/', views.RegisterView.as_view(),),
    # url(r'login/', views.LoginView.as_view(), ),
    url(r'show_info/$',views.show_info,),
    url(r'login/$',views.login,),
    url(r'register/$',views.register,),
    url(r'profile/$',views.profile,),
    url(r'getUserProfile/$',views.getUserProfile,),
    url(r'submitOrder/$',views.submitOrder),
    url(r'getOrderHistory/$',views.getOrderHistory)
    # url(r'login/$', views.LoginView.as_view()),
    # url(r'register$/',views.RegisterView.as_view()),
	# path('index', views.index, name='index')
	# path(r'login',view.LoginView.as_view(), name= 'user_login')

	
]