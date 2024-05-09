from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'role', 'birthday', 'first_name', 'last_name', 'password1', 'password2']


# class CustomPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}))
#     new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
#     new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))