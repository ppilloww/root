from django.urls import path
from bbq_gmbh_app.views import *

# Administrationsbereich von Django, kann als url/admin zugegriffen werden
urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('home/', home, name='home'),
    path('changePassword/', changePassword, name='changePassword'),
    path('employeeManagement/', employeeManagement, name='employeeManagement'),
    path('profile/', profile, name='profile'),
    path('checkHolidays/', checkHolidays, name='checkHolidays'),
    path('get_user_role/', get_user_role, name='get_user_role'),
    path('user_view/', user_view, name='user_view'),
    path('addUser/', addUser, name='addUser'),
    path('logout_view/', logout_view, name='logout'),
]

