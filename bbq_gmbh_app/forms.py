# Description: This file contains the forms for the bbq_gmbh_app application.
# The forms are used to create the user interface for the application.
# Even though the forms are not directly used in the views, they are used
# in the templates to create the user interface.
# All fields are required in the forms!

from django.contrib.auth.forms import UserCreationForm
from django import forms
from bbq_gmbh_app.models import Mitarbeiter, Adresse, Arbeitsstunden
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from datetime import date, timedelta
import requests



class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['strasse', 'stadt', 'plz', 'land']

    def clean_stadt(self):
        stadt = self.cleaned_data.get('stadt')
        land = self.cleaned_data.get('land')
        print('form Stadt', stadt, 'form Land', land)

        if stadt and land:
            response = requests.get(f'http://geodb-free-service.wirefreethought.com/v1/geo/cities?countryIds={land}&namePrefix={stadt}')
            data = response.json()

            # Check if the city exists in the country
            if not data['data']:
                raise ValidationError("The city doesn't match the country.")

        return stadt

class CreateUserForm(UserCreationForm):
    adresse = AdresseForm() # never touch a running system !!
    class Meta:
        model = Mitarbeiter
        fields = ['email', 'role', 'birthday', 'first_name', 'last_name', 'gender', 'adresse', 'wochenarbeitszeit', 'password1', 'password2']

    # This is handling the age validation
    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        today = date.today()

        if birthday > today - timedelta(days=16*365.25):
            raise forms.ValidationError("You must be at least 16 years old.")
        if birthday < today - timedelta(days=150*365.25):
            raise forms.ValidationError("Invalid age. Are you sure, this person is still alive?")

        return birthday


class CheckInForm(forms.ModelForm):
    class Meta:
        model = Arbeitsstunden
        fields = ['datum', 'beginn', 'status']

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Arbeitsstunden
        fields = ['datum', 'ende', 'status']

# This is handling the password change validation
# The new password cannot be the same as the old password
class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        if old_password == new_password1:
            raise ValidationError("New password cannot be the same as the old password.")

        return new_password1