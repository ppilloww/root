from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, birthday, gender, role, address,  password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        if not last_name:
            raise ValueError('The Last Name field must be set')
        if not birthday:
            raise ValueError('The Birthday field must be set')
        if not gender:
            raise ValueError('The Gender field must be set')
        if not role:
            raise ValueError('The Role field must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            gender=gender,
            role=role,
            address=address,
            

        )
        user.set_password(password) # hash
        user.save(using=self._db) # for multiple databases
        return user
    
    def create_superuser(self, email, first_name, last_name, birthday, gender, role, address, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            gender=gender,
            role=role,
            password=password,
            address=address,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.street

class CustomUser(AbstractBaseUser):

    ROLE_CHOICES = [
        ('user', 'User'),
        ('hr', 'HR'),
        ('admin', 'Admin'),
    ]

    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True) 
    email = models.EmailField('email address', unique=True)
    birthday = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)

    # required fields
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'gender']

    objects = CustomUserManager()



    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label): # only for admin
        return True