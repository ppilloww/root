from typing import Any
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.

######################################### Database operations #########################################

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, adresse, role, birthday, week_hours, gender, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        if not last_name:
            raise ValueError('The Last Name field must be set')
        if not adresse:
            raise ValueError('The Adresse field must be set')
        if not role:
            raise ValueError('The Role field must be set')
        if not birthday:
            raise ValueError('The Birthday field must be set')
        if not week_hours:
            raise ValueError('The Week Hours field must be set')
        if not gender:
            raise ValueError('The Gender field must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            adresse=adresse,
            role=role,
            birthday=birthday,
            week_hours=week_hours,

        )
        user.set_password(password) # hash
        user.save(using=self._db) # for multiple databases
        return user
    
    def create_superuser(self, email, first_name, last_name, adresse, role, birthday, week_hours, gender, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            adresse=adresse,
            role=role,
            birthday=birthday,
            password=password,
            gender=gender,
            week_hours=week_hours,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
def get_default_adresse():
    return Adresse.objects.get_or_create(street='Default Street', city='Default City', state='Default State', zip_code='Default Zip Code')[0].id

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('hr', 'HR'),
        ('admin', 'Admin'),
    ]
    WEEK_HOUR_CHOICES = [
        (30, '30'),
        (35, '35'),
        (40, '40'),
    ]
        
    email = models.EmailField('email address', unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    birthday = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    week_hours = models.IntegerField(choices=WEEK_HOUR_CHOICES, default=35)
    adresse = models.ForeignKey("Adresse", on_delete=models.PROTECT, default=get_default_adresse, related_name="customuser")
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    urlaubstage = models.IntegerField(default=30, null=True, blank=True)
    job_title = models.CharField(max_length=225, null=True, blank=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'birthday', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label): # only for admin
        return True

class Adresse(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

######################################### Database operations #########################################
