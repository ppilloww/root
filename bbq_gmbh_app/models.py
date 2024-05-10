from typing import Any
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.

######################################### Database operations #########################################

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, role, birthday, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        if not last_name:
            raise ValueError('The Last Name field must be set')
        if not role:
            raise ValueError('The Role field must be set')
        if not birthday:
            raise ValueError('The Birthday field must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            birthday=birthday,

        )
        user.set_password(password) # hash
        user.save(using=self._db) # for multiple databases
        return user
    
    def create_superuser(self, email, first_name, last_name, role, birthday, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            birthday=birthday,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('hr', 'HR'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField('email address', unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    birthday = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    

    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'birthday', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label): # only for admin
        return True


######################################### Database operations #########################################
