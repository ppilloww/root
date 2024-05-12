from django import forms
from django.contrib.auth.forms import UserCreationForm
from bbq_gmbh_app.models import CustomUser, Adresse

class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['street', 'zip_code', 'city']

class CreateUserForm(UserCreationForm):
    adresse = AdresseForm()
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'adresse', 'role', 'birthday', 'week_hours', 'gender', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     adresse = self.cleaned_data.pop('adresse')
    #     if commit:
    #         adresse_form = AdresseForm(adresse)
    #         if adresse_form.is_valid():
    #             user.adresse = adresse_form.save()
    #             user.save()
    #     return user