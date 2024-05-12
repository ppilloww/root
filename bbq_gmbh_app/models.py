from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, role, birthday, week_hours, gender, password=None):
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
        if not week_hours:
            raise ValueError('The Week Hours field must be set')
        if not gender:
            raise ValueError('The Gender field must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            birthday=birthday,
            week_hours=week_hours,
            gender=gender,

        )
        user.set_password(password) # hash
        user.save(using=self._db) # for multiple databases
        return user
    
    def create_superuser(self, email, first_name, last_name, role, birthday, week_hours, gender, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
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
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    urlaubstage = models.IntegerField(default=30, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)

    # required fields
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday']

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",
        related_query_name="customuser",
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_user_permissions",
        related_query_name="customuser",
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label): # only for admin
        return True