from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from loginApp.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_home(request):
    return render(request, 'staffApp/home.html')
