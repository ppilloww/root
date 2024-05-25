from django.contrib.auth.forms import UserCreationForm
from django import forms
from bbq_gmbh_app.models import Mitarbeiter



class CreateUserForm(UserCreationForm):
    class Meta:
        model = Mitarbeiter
        fields = ['email', 'role', 'birthday', 'first_name', 'last_name', 'gender', 'password1', 'password2']

