from django.contrib import admin

# Register your models here.
from user.models import UserInfo, Profile
admin.site.register(UserInfo)
admin.site.register(Profile)
