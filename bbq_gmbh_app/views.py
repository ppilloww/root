from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'indexEn.html')

def signin(request):
    return render(request, 'signinEn.html')

def home(request):
    return render(request, 'homeEnHr.html')

def changePassword(request):
    return render(request, 'pwEn.html')

def employeeManagement(request):
    return render(request, 'employeeManagementEn.html')

def profile(request):
    return render(request, 'profileEn.html')
