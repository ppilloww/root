from django.contrib.auth.forms import UserCreationForm
from bbq_gmbh_app.models import CustomUser, Address
from django import forms

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'country', 'zip_code']

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = False
        self.fields['mobile_phone'].required = False
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'birthday', 'gender', 'role', 'password1', 'password2',
                   'phone', 'mobile_phone', 'address']
        

