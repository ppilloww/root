from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from bbq_gmbh_app.forms import CreateUserForm
from bbq_gmbh_app.models import Mitarbeiter
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from datetime import date



# Create your views here.
def index(request):
    return render(request, 'bbq_gmbh_app/index.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user = authenticate(request, email=email, password=password)
        print('user is', user)

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

@login_required
def get_user_role(request):
    return JsonResponse({'user_role': request.user.role})

@login_required(login_url='signin')
def home(request):
    return render(request, 'bbq_gmbh_app/home.html')

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
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'bbq_gmbh_app/changePassword.html',  {'form': form})

def userLogout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='signin')
def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('employeeManagement')

    else:
        form = CreateUserForm()
    return render(request, 'bbq_gmbh_app/createUser.html', {'form': form})

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

