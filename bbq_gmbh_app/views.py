from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from bbq_gmbh_app.forms import CreateUserForm
from bbq_gmbh_app.models import CustomUser
from django.http import JsonResponse, HttpResponse
from datetime import date, datetime
import holidays



# Create your views here.
def index(request):
    return render(request, 'indexEn.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                request.session['user_role'] = user.role
                return JsonResponse({'status': 'success', 'user_role': user.role}, status=200)
            else:
                return JsonResponse({'status': 'inactive'}, status=401)
        else:
            return JsonResponse({'status': 'invalid'}, status=401)
        
    return render(request, 'signinEn.html')

def home(request):
    return render(request, 'homeEnHr.html')

def changePassword(request):
    return render(request, 'pwEn.html')

# def employeeManagement(request):
#     user_view_response = user_view(request)
#     if 'error' in user_view_response:
#         return JsonResponse({'error': 'User not found'})
#     employees = user_view_response['employees']
#     return render(request, 'employeeManagementEn.html', {'employees': employees})
def employeeManagement(request):
    user_id = request.session.get('user_id', None)
    if user_id is None:
        return JsonResponse({'error': 'User not found'})
    employees = CustomUser.objects.all()
    return render(request, 'employeeManagementEn.html', {'employees': employees})

def profile(request):
    return render(request, 'profileEn.html')

def addUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeManagement')
    else:
        form = CreateUserForm()
    return render(request, 'addUser.html', {'form': form})

def bye(request):
    return render(request, 'bye.html')



######################################### authentcation #########################################

def get_user_role(request):
    user_role = request.session.get('user_role', None)
    if user_role is None:
        return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'user_role': user_role})

# def log out and flush session
def logout_view(request):
    logout(request)
    return redirect('bye')

######################################### authentcation #########################################

######################################### Logics #########################################

# checkig publick holidays
def checkHolidays(request):
    today = date.today()
    de_holidays = holidays.Germany(prov='BW')
    is_public_holiday = today in de_holidays
    is_sunday = today.weekday() == 6 #6 = sunday
    context = {'non_working_day': False } #is_public_holiday or is_sunday
    return JsonResponse(context)

# get all employees
# def user_view(request):
#     user_id = request.session.get('user_id', None)
#     print("User_view_id:", user_id)
#     if user_id is not None:
#         # print("User_view:", user_id)
#         employees = CustomUser.objects.all()
#         print(employees)
#         # return render(request, "employeeManagementEn.html", {'employees': employees})
#         return {'employees': employees}
#     return JsonResponse({'error': 'User not found'})

# get user information

######################################### Logics #########################################

######################################### Database operations #########################################




######################################### Database operations #########################################
