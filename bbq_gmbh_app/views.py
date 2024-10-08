from bbq_gmbh_app.forms import CreateUserForm, AdresseForm, CheckInForm, CheckOutForm, CustomPasswordChangeForm, UrlaubForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from bbq_gmbh_app.models import Mitarbeiter, Arbeitsstunden, Urlaub
from django.http import JsonResponse
from django.contrib import messages
from datetime import date, datetime
from django.utils import timezone


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
                if user.must_change_password:
                    return redirect('newPassword')
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
    arbeitsstunden = Arbeitsstunden.objects.filter(mitarbeiter=request.user)
    weekHours = request.user.wochenarbeitszeit.total_seconds() / 3600
    urlaub = Urlaub.objects.filter(mitarbeiter=request.user)

    return render(request, 'bbq_gmbh_app/home.html', {'arbeitsstunden': arbeitsstunden,
                                                        'weekHours': weekHours,
                                                        'urlaub': urlaub,
                                                        })

# This ishandling the refreshing of the time table
@login_required(login_url='signin')
def arbeitsstunden(request):
    arbeitsstunden = Arbeitsstunden.objects.filter(mitarbeiter=request.user)
    return render(request, 'bbq_gmbh_app/_timeTable.html', {'arbeitsstunden': arbeitsstunden})

# This is handling the refreshing of the info box
@login_required(login_url='signin')
def infoBox(request):
    
    sessionAge = request.session.get_expiry_age()

    # print('sessionAge', sessionAge)
    return render(request, 'bbq_gmbh_app/_infoBox.html')

# This view is used to display all users
# It is fetching all users from the database
# and passing them to the template
# easy
@login_required(login_url='signin')
def employeeManagement(request):
    users = Mitarbeiter.objects.all()
    if request.user.role == 'Admin':
        role = True
    else:
        role = False

    return render(request, 'bbq_gmbh_app/employeeManagement.html', {'users': users, 'role': role})

@login_required(login_url='signin')
def profile(request):
    arbeitsstunden = Arbeitsstunden.objects.filter(mitarbeiter=request.user)
    
    return render(request, 'bbq_gmbh_app/profile.html', {'arbeitsstunden': arbeitsstunden})

@login_required(login_url='signin')
def changePassword(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Changing password failed. Please correct the error below')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'bbq_gmbh_app/changePassword.html',  {'form': form})

# This view is to force the user to change the password
@login_required(login_url='signin')
def newPassword(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            user.must_change_password = False
            user.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Changing password failed. Please correct the error below')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'bbq_gmbh_app/newPassword.html',  {'form': form})

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
        urlaubForm = UrlaubForm(request.POST)
        # print("request.POST", request.POST)
        if userForm.is_valid() and adresseForm.is_valid() and urlaubForm.is_valid():
            user = userForm.save(commit=False)
            adresse = adresseForm.save()
            user.adresse = adresse
            user.save()
            urlaub = urlaubForm.save(commit=False)
            urlaub.mitarbeiter = user
            urlaub.save()

            return redirect('employeeManagement')
    else:
        userForm = CreateUserForm()
        adresseForm = AdresseForm()
        urlaubForm = UrlaubForm()
    return render(request, 'bbq_gmbh_app/createUser.html', {
        'userForm': userForm, 
        'adresseForm': adresseForm,
        'urlaubForm': urlaubForm
        })


login_required(login_url='signin')
def userDetail(request, user_id):
    user = Mitarbeiter.objects.get(id=user_id)
    arbeitsstunden = Arbeitsstunden.objects.filter(mitarbeiter=user)
    urlaub = Urlaub.objects.filter(mitarbeiter=user)
    weekHours = request.user.wochenarbeitszeit.total_seconds() / 3600
    activeStatus = user.is_active
    if request.method == "POST":
        if 'action' in request.POST:
            if request.POST['action'] == 'Delete User':
                user.is_active = False
                user.save()
                pass
            elif request.POST['action'] == 'Activate User':
                user.is_active = True
                user.save()
                pass


    return render(request, 'bbq_gmbh_app/userDetail.html', {'user': user,
                                                            'arbeitsstunden': arbeitsstunden,
                                                            'urlaub': urlaub,
                                                            'weekHours': weekHours,
                                                            'activeStatus': activeStatus,
                                                            })

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

    # This is handling a cross block of the checkIn and checkOut status
    # if the last Arbeitsstunden object of the currently logged in user
        # has the status 'True' the checkInStatus is set to True and the user can't check in again
    # if the last Arbeitsstunden object of the currently logged in user
        # has the status 'False' the checkOutStatus is set to False and the user can't check out again
    # .exists() is used to check if the user has any Arbeitsstunden objects in the database at all
        # if not the checkOutStatus is set to True and the user can't check out again until he checked in
    if Arbeitsstunden.objects.filter(mitarbeiter=request.user).exists():
        checkInStatus = Arbeitsstunden.objects.filter(mitarbeiter=request.user).last()
        checkInStatus = checkInStatus.status
        checkOutStatus = Arbeitsstunden.objects.filter(mitarbeiter=request.user).last()
        checkOutStatus = not checkOutStatus.status
    else:
        checkOutStatus = True
        checkInStatus = False

    # This is handling the allowed working hours
    # if the current time is between 06:00 and 22:00 the user can check in
    # else the user can't check in
    now = datetime.now()
    startWorkingHours = now.replace(hour=6, minute=0, second=0, microsecond=0)
    endWorkingHours = now.replace(hour=22, minute=0, second=0, microsecond=0)
    if now < startWorkingHours or now > endWorkingHours:
        allowedWorkingHours = False
    else:
        allowedWorkingHours = True

    context = {'non_working_day': is_public_holiday or is_sunday,
                'checkInStatus': checkInStatus,
                'checkOutStatus': checkOutStatus,
                'allowedWorkingHours': allowedWorkingHours,
    }

    # print('checkInStatus', checkInStatus)
    # print('checkOutStatus', checkOutStatus)

    return JsonResponse(context)

# This view is used to check in a user
# It is handling the CheckInForm and setting the user
# and the status of the Arbeitsstunden object
# to the currently logged in user and 'checked_in'
@login_required(login_url='signin')
def checkIn(request):
    if request.method == 'POST':
        checkInForm = CheckInForm(request.POST)
        if checkInForm.is_valid():
            checkIn = checkInForm.save(commit=False)
            checkIn.datum = timezone.localdate()
            checkIn.beginn = timezone.localtime().time()
            checkIn.mitarbeiter = request.user
            checkIn.save()
            checkInStatus = checkIn.status # handling too late! set this to home view
            return redirect('home')
    else:
        checkInForm = CheckInForm()
    return render(request, 'bbq_gmbh_app/home.html', {'checkInForm': checkInForm})

# This view is used to check out a user
# It is handling the CheckOutForm and setting the user
# and the status of the Arbeitsstunden object
# to the currently logged in user and 'checked_out'
@login_required(login_url='signin')
def checkOut(request):
    if request.method == 'POST':
        try:
            # This is handling the mathod to write the end time to the last Arbeitsstunden object
            arbeitsstunde = Arbeitsstunden.objects.filter(mitarbeiter=request.user, datum=timezone.localdate()).latest('id')
        except ObjectDoesNotExist:
            arbeitsstunde = Arbeitsstunden(mitarbeiter=request.user, datum=timezone.localdate())
        
        checkOutForm = CheckOutForm(request.POST, instance=arbeitsstunde)
        if checkOutForm.is_valid():
            checkOut = checkOutForm.save(commit=False)
            checkOut.datum = timezone.localdate()
            checkOut.ende = timezone.localtime().time()
            checkOut.mitarbeiter = request.user
            checkOut.save()
            checkOutStatus = checkOut.status # handling too late! set this to home view
            return redirect('home')
    else:
        checkOutForm = CheckOutForm()
    return render(request, 'bbq_gmbh_app/home.html', {'checkOutForm': checkOutForm})


