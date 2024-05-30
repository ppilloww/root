# Read Me: This file contains the models for Mitarbeiter 
# and the custom manager for Mitarbeiter. The Mitarbeiter model
# is a custom user model that extends the AbstractUser model
# from Django.
# Ensure that superusers can change the password of other users
# but it will no be hashed.
# Its generally a good idea to create a new user outside of the Admin 
# interface and edit the user in the Admin interface.


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class MitarbeiterManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# this is the maincharakter of the app !!
# this is the user model
# evry changes MUST be migrated very carefully
class Mitarbeiter(AbstractUser):
    ROLE_CHOICES = [
        ('User', 'User'),
        ('Hr', 'HR'),
        ('Admin', 'Admin'),
    ]
    

    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    # extra fields which are not required in the backend
    # but can be required in the frontend
    birthday = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)
    adresse = models.ForeignKey('Adresse', on_delete=models.PROTECT, null=True, blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MitarbeiterManager()



    def __str__(self):
        return self.email
    


class Adresse(models.Model):

    strasse = models.CharField(max_length=100)
    stadt = models.CharField(max_length=100)
    plz = models.CharField(max_length=10)
    land = CountryField(default='DE')
    

    def __str__(self):
        return f'{self.strasse}, {self.stadt}, {self.plz}, {self.land}'
    
class Arbeitsstunden(models.Model):
        
        PAUSE_CHOICES = [
            ('01:00', '1:00'),
            ('00:45', '0:45'),
            ('00:30', '0:30'),
            ('00:15', '0:15'),
            ('00:00', '0:00'),
        ]
        
    
        mitarbeiter = models.ForeignKey(Mitarbeiter, on_delete=models.CASCADE)
        datum = models.DateField(blank=True, null=True)
        beginn = models.TimeField(blank=True, null=True)
        ende = models.TimeField(blank=True, null=True)
        pause = models.TimeField(choices=PAUSE_CHOICES, default='01:00')
        stunden = models.TimeField(default='08:00')
        ueberstunden = models.TimeField(default='00:00')
        status = models.BooleanField(default=False)
    
        def __str__(self):
            return f'{self.mitarbeiter} - {self.datum} - {self.beginn} - {self.ende} - {self.stunden}h - {self.ueberstunden}h - {self.status}'