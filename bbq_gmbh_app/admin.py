from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Adresse

# Register your models here.


######################################### Database operations #########################################
 
admin.site.register(CustomUser)
admin.site.register(Adresse)

######################################### Database operations #########################################