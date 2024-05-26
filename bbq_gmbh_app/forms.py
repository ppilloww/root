from django.contrib.auth.forms import UserCreationForm
from django import forms
from bbq_gmbh_app.models import Mitarbeiter, Adresse



class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['strasse', 'stadt', 'plz', 'land']

class CreateUserForm(UserCreationForm):
    adresse = AdresseForm()
    class Meta:
        model = Mitarbeiter
        fields = ['email', 'role', 'birthday', 'first_name', 'last_name', 'gender', 'adresse', 'password1', 'password2']



