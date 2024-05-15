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
    path('get_user_role/', get_user_role, name='get_user_role'),
    path('logout_view/', logout_view, name='logout_view'),
    path('profile/', profile, name='profile'),
]
