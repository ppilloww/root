from django import forms
from django.contrib.auth.forms import UserCreationForm
from bbq_gmbh_app.models import CustomUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'role', 'birthday', 'password1', 'password2']