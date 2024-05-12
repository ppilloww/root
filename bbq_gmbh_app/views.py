from django.contrib.auth import authenticate, login, logout
from bbq_gmbh_app.forms import CreateUserForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import date
import holidays

# Create your views here.
def index(request):
    return render(request, 'bbq_gmbh_app/indexEn.html')

def signin(request):
    return render(request, 'bbq_gmbh_app/signinEn.html')

def home(request):
    return render(request, 'bbq_gmbh_app/homeEnHr.html')

def changePassword(request):
    return render(request, 'bbq_gmbh_app/pwEn.html')

def employeeManagement(request):
    return render(request, 'bbq_gmbh_app/employeeManagementEn.html')

def profile(request):
    return render(request, 'bbq_gmbh_app/profileEn.html')

def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeManagement')
    else:
        form = CreateUserForm()
    return render(request, 'bbq_gmbh_app/createUser.html', {'form': form})

# checkig publick holidays
def checkHolidays(request):
    today = date.today()
    de_holidays = holidays.Germany(prov='BW')
    is_public_holiday = today in de_holidays
    is_sunday = today.weekday() == 6 #6 = sunday
    context = {'non_working_day': False } #is_public_holiday or is_sunday
    return JsonResponse(context)
