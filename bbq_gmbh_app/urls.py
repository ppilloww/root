from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('employeeManagement/', views.employeeManagement, name='employeeManagement'),
    path('profile/', views.profile, name='profile'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('logout/', views.userLogout, name='logout'),
    path('createUser/', views.createUser, name='createUser'),
    
]
