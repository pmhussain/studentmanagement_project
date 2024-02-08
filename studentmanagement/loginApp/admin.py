from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username','first_name', 'last_name','email','designation', 'mobileno', 'profile_pic']
admin.site.register(CustomUser,CustomUserAdmin)
