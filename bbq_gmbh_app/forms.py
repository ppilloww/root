from django.contrib.auth.forms import UserCreationForm
from django import forms
from bbq_gmbh_app.models import Mitarbeiter, Adresse, Arbeitsstunden
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError



class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['strasse', 'stadt', 'plz', 'land']

class CreateUserForm(UserCreationForm):
    adresse = AdresseForm()
    class Meta:
        model = Mitarbeiter
        fields = ['email', 'role', 'birthday', 'first_name', 'last_name', 'gender', 'adresse', 'password1', 'password2']


class CheckInForm(forms.ModelForm):
    class Meta:
        model = Arbeitsstunden
        fields = ['datum', 'beginn', 'status']

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Arbeitsstunden
        fields = ['datum', 'ende', 'status']


class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        if old_password == new_password1:
            raise ValidationError("New password cannot be the same as the old password.")

        return new_password1