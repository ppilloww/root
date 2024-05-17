from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from bbq_gmbh_app.forms import CreateUserForm, AddressForm
from django.shortcuts import render, redirect
from bbq_gmbh_app.models import CustomUser
from django.http import JsonResponse
from django.contrib import messages
from datetime import date
import holidays

# Create your views here.
def index(request):
    return render(request, 'bbq_gmbh_app/indexEn.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_role'] = user.role
                return JsonResponse({'status': 'success', 'user_role':user.role}, status=200)
            else:
                return JsonResponse({'status': 'inactive'}, status=401)
        else:
            return JsonResponse({'status': 'invalid'}, status=401)
    return render(request, 'bbq_gmbh_app/signinEn.html')

@login_required(login_url='signin')
def home(request):
    return render(request, 'bbq_gmbh_app/homeEnHr.html')

@login_required(login_url='signin')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'bbq_gmbh_app/pwEn.html', {'form': form})

@login_required(login_url='signin')
def employeeManagement(request):
    users = CustomUser.objects.all()
    return render(request, 'bbq_gmbh_app/employeeManagementEn.html', {'users': users})

@login_required(login_url='signin')
def profile(request):
    return render(request, 'bbq_gmbh_app/profileEn.html')

@login_required(login_url='signin')
def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Parse address data from POST request
            address_data = {
                'street': request.POST.get('address.street'),
                'city': request.POST.get('address.city'),
                'country': request.POST.get('address.country'),
                'zip_code': request.POST.get('address.zip_code')
            }
            # Create Address object
            address_form = AddressForm(address_data)
            if address_form.is_valid():
                address = address_form.save()

                user = form.save(commit=False)
                user.address = address
                user.save()

                return redirect('employeeManagement')
    else:
        form = CreateUserForm()
    return render(request, 'bbq_gmbh_app/createUser.html', {'form': form})

@login_required(login_url='signin')
def profile(request):
    return render(request, 'bbq_gmbh_app/profile.html')

@login_required(login_url='signin')
def userDetail(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('bbq_gmbh_app/', user_id=user.id)
    else:
        form = CreateUserForm(instance=user)
    return render(request, 'bbq_gmbh_app/userDetail.html', {'user': user, 'form': form})


@login_required
def get_user_role(request):
    return JsonResponse({'user_role': request.user.role})


def logout_view(request):
    return render(request, 'bbq_gmbh_app/bye.html')

def userLogout(request):
    logout(request)
    return redirect('logout_view')







# checkig publick holidays
def checkHolidays(request):
    today = date.today()
    de_holidays = holidays.Germany(prov='BW')
    is_public_holiday = today in de_holidays
    is_sunday = today.weekday() == 6 #6 = sunday
    context = {'non_working_day': False } #is_public_holiday or is_sunday
    return JsonResponse(context)
