from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from bbq_gmbh_app.models import Mitarbeiter
from django.http import JsonResponse
from django.contrib import messages
from datetime import date



# Create your views here.
def index(request):
    return render(request, 'bbq_gmbh_app/index.html')

def signin(request):
    return render(request, 'bbq_gmbh_app/signin.html')

def home(request):
    return render(request, 'bbq_gmbh_app/home.html')

def employeeManagement(request):
    return render(request, 'bbq_gmbh_app/employeeManagement.html')

def profile(request):
    return render(request, 'bbq_gmbh_app/profile.html')

def changePassword(request):
    return render(request, 'bbq_gmbh_app/changePassword.html')

def userLogout(request):
    logout(request)
    return redirect('index')

def createUser(request):
    return render(request, 'bbq_gmbh_app/createUser.html')