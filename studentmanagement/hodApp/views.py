from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from loginApp.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
@admin_only
def hod_home(request):
    return render(request, 'hodApp/home.html')
