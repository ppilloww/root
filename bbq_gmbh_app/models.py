from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.

######################################### Database operations #########################################

class CustomUserManager(BaseUserManager):
    def create_user(self, email, role, birthday, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not role:
            raise ValueError('The Role field must be set')
        if not birthday:
            raise ValueError('The Birthday field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        if not last_name:
            raise ValueError('The Last Name field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, birthday=birthday, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, birthday, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, role, birthday, first_name, last_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('user', 'User'),
    ]
    email = models.EmailField('email address', unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    birthday = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'birthday', 'first_name', 'last_name']


######################################### Database operations #########################################
