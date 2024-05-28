from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.shortcuts import render, redirect
from bbq_gmbh_app.forms import CreateUserForm, AdresseForm, CheckInForm, CheckOutForm
from bbq_gmbh_app.models import Mitarbeiter
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from datetime import date, datetime
import holidays



# Create your views here.
def index(request):
    return render(request, 'bbq_gmbh_app/index.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_role'] = user.role
                return JsonResponse({'status': 'success', 'user_role':user.role}, status=200)
            else:
                return JsonResponse({'status': 'inactive'}, status=401)
        else:
            return JsonResponse({'status': 'invalid'}, status=401)
    return render(request, 'bbq_gmbh_app/signin.html')

# This is a custom view that returns the user role
# of the currently logged in user
# which is nessesery to set the navigation links on the frontend
# based on the user role.

def get_user_role(request):
    if request.user.is_authenticated:
        return JsonResponse({'user_role': request.user.role})
    else:
        return JsonResponse({'status': 'not authenticated'}, status=401)

@login_required(login_url='signin')
def home(request):
    return render(request, 'bbq_gmbh_app/home.html')

# This view is used to display all users
# It is fetching all users from the database
# and passing them to the template
# easy
@login_required(login_url='signin')
def employeeManagement(request):
    users = Mitarbeiter.objects.all()

    return render(request, 'bbq_gmbh_app/employeeManagement.html', {'users': users})

@login_required(login_url='signin')
def profile(request):
    return render(request, 'bbq_gmbh_app/profile.html')

@login_required(login_url='signin')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Changing password failed. Please correct the error below')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'bbq_gmbh_app/changePassword.html',  {'form': form})

def userLogout(request):
    logout(request)
    return redirect('index')


# This view is used to create a new user
# It is handling the CreateUserForm and the AdresseForm
# The CreateUserForm is a custom form that extends the UserCreationForm
# from Django and adds an AdresseForm to it.
@login_required(login_url='signin')
def createUser(request):
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        adresseForm = AdresseForm(request.POST)
        # print("request.POST", request.POST)
        if userForm.is_valid() and adresseForm.is_valid():
            user = userForm.save(commit=False)
            adresse = adresseForm.save()
            user.adresse = adresse
            user.save()
            return redirect('employeeManagement')
    else:
        userForm = CreateUserForm()
        adresseForm = AdresseForm()
    return render(request, 'bbq_gmbh_app/createUser.html', {
        'userForm': userForm, 
        'adresseForm': adresseForm
        })
# def createUser(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         print('form',form)
#         if form.is_valid():

#             form.save()
#             return redirect('employeeManagement')

#     else:
#         form = UserCreationForm()
#     return render(request, 'bbq_gmbh_app/createUser.html', {'form': form})

login_required(login_url='signin')
def userDetail(request, user_id):
    user = Mitarbeiter.objects.get(id=user_id)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('bbq_gmbh_app/', user_id=user.id)
    else:
        form = CreateUserForm(instance=user)
    return render(request, 'bbq_gmbh_app/userDetail.html', {'user': user, 'form': form})

# This view is used to check if today is a public holiday
# or a sunday. It is returning a JsonResponse with a boolean
# for testing purposes set the non_working_day to True if today is a public holiday or a sunday
# and to False if today is a working day
# else {'non_working_day': is_public_holiday or is_sunday}
def checkHolidays(request):
    today = date.today()
    de_holidays = holidays.Germany(prov='BW')
    is_public_holiday = today in de_holidays
    is_sunday = today.weekday() == 6 #6 = sunday
    context = {'non_working_day': is_public_holiday or is_sunday }
    return JsonResponse(context)




