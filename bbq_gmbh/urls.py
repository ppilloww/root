"""
URL configuration for bbq_gmbh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bbq_gmbh_app.views import *

# Administrationsbereich von Django, kann als url/admin zugegriffen werden
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('index/', index, name='index'),
    path('signin/', signin, name='signin'),
    path('home/', home, name='home'),
    path('changePassword/', changePassword, name='changePassword'),
    path('employeeManagement/', employeeManagement, name='employeeManagement'),
    path('profile/', profile, name='profile'),
    path('checkHolidays/', checkHolidays, name='checkHolidays'),
    path('login_view/', login_view, name='login_view'),
    path('get_user_role/', get_user_role, name='get_user_role'),
]

