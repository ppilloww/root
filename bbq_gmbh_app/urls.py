from django.urls import path
from bbq_gmbh_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('home/', home, name='home'),
    path('changePassword/', changePassword, name='changePassword'),
    path('employeeManagement/', employeeManagement, name='employeeManagement'),
    path('profile/', profile, name='profile'),
    path('checkHolidays/', checkHolidays, name='checkHolidays'),
    path('createUser/', createUser, name='createUser'),
    path('userLogout/', userLogout, name='userLogout'),
]
