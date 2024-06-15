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
from datetime import timedelta, datetime, date
from django.db.models import Sum


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
        user.must_change_password = True
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
        extra_fields.setdefault('must_change_password', False)

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
    WOCHENARBEITSZEIT_CHOICES = [
        (timedelta(hours=40), '40:00'),
        (timedelta(hours=35), '35:00'),
        (timedelta(hours=30), '30:00'),
    ]
    

    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    must_change_password = models.BooleanField(default=True)

    # extra fields which are not required in the backend
    # but can be required in the frontend
    birthday = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)
    adresse = models.ForeignKey('Adresse', on_delete=models.PROTECT, null=True, blank=True)
    wochenarbeitszeit = models.DurationField(choices=WOCHENARBEITSZEIT_CHOICES, blank=True, null=True)



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

# This is handling the calculation of the age
def calculate_age(birthdate):
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


class Arbeitsstunden(models.Model):
    PAUSE_CHOICES = [
    (timedelta(hours=1), '1:00'),
    (timedelta(minutes=45), '0:45'),
    (timedelta(minutes=30), '0:30'),
    (timedelta(minutes=15), '0:15'),
    (timedelta(minutes=0), '0:00'),
    ]        
    
    mitarbeiter = models.ForeignKey(Mitarbeiter, on_delete=models.CASCADE)
    datum = models.DateField(blank=True, null=True)
    beginn = models.TimeField(blank=True, null=True)
    ende = models.TimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    # This is handling the calculation of the working hours
    pause = models.DurationField(choices=PAUSE_CHOICES, default=timedelta(hours=1))
    arbeitszeitTag = models.DurationField(default=timedelta())
    minArbeitszeitTag = models.DurationField(default=timedelta())
    maxArbeitszeitTag = models.DurationField(default=timedelta(hours=10))
    averageArbeitszeit = models.DurationField(default=timedelta())
    gleitzeitTag = models.DurationField(default=timedelta())
    ueberstunden = models.DurationField(default=timedelta())
    arbeitszeitGes = models.DurationField(default=timedelta())



    def calculateArbeitszeit(self):

        # This is handling the calculation of the minimum working hours per day
        self.minArbeitszeitTag = self.mitarbeiter.wochenarbeitszeit / 5

        if self.datum and self.beginn and self.ende:
            beginn_dt = datetime.combine(self.datum, self.beginn)
            ende_dt = datetime.combine(self.datum, self.ende)
            pause = timedelta(hours=self.pause.seconds//3600, minutes=(self.pause.seconds//60)%60) # dont forget to calculate the pause

            # This is handling the worked hours per day
            arbeitszeit = (ende_dt - beginn_dt) - pause

            # This is handling the calculation of the working hours per day
            self.arbeitszeitTag = arbeitszeit - self.minArbeitszeitTag

            # This is handling the calculation of the flextime per day
            if self.arbeitszeitTag > self.minArbeitszeitTag:
                self.gleitzeitTag = self.arbeitszeitTag - self.minArbeitszeitTag


            # This is handling the calculation of the maximum working hours per day based on the age
            age = calculate_age(self.mitarbeiter.birthday)
            
            twenty_four_weeks_ago = datetime.now().date() - timedelta(weeks=24)
            average_arbeitszeit = Arbeitsstunden.objects.filter(mitarbeiter=self.mitarbeiter, 
                                                                datum__gte=twenty_four_weeks_ago).aggregate(Sum('arbeitszeitTag'))['arbeitszeitTag__sum'] / 24 # calculate the average working hours of the employee in the last 24 weeks

            if age >= 15 and age < 18:
                self.averageArbeitszeit = average_arbeitszeit if average_arbeitszeit < timedelta(hours=8) else timedelta(hours=8.5)
                self.maxArbeitszeitTag = timedelta(hours=8.5)
            else:
                self.averageArbeitszeit = average_arbeitszeit if average_arbeitszeit < timedelta(hours=8) else timedelta(hours=10)
                self.maxArbeitszeitTag = timedelta(hours=10)

             


            # This is handling the total working hours of the employee
            # total_arbeitszeit = Arbeitsstunden.objects.filter(mitarbeiter=self.mitarbeiter).aggregate(Sum('arbeitszeitTag'))['arbeitszeitTag__sum'] # sum up all the working hours of the employee
            # self.arbeitszeitGes = total_arbeitszeit if total_arbeitszeit else timedelta() # if there are no working hours, set the total working hours to 0

            # # This is handling the total overtimes ofthe employee
            # glleitzeit = Arbeitsstunden.objects.filter(mitarbeiter=self.mitarbeiter).aggregate(Sum('gleitzeitTag'))['gleitzeitTag__sum'] # sum up all the flextime of the employee
            # self.ueberstunden = self.arbeitszeitGes - glleitzeit if self.arbeitszeitGes > glleitzeit else timedelta()
            # self.save()

            # Accumulate work time and calculate overtime
            # arbeitsstunden_all = Arbeitsstunden.objects.filter(mitarbeiter=self.mitarbeiter, datum__week=self.datum.isocalendar()[1])
            # total_arbeitszeit = sum((a.arbeitszeitTag for a in arbeitsstunden_all), timedelta())

            # self.arbeitszeitGes = total_arbeitszeit
            # self.ueberstunden = total_arbeitszeit - self.mitarbeiter.wochenarbeitszeit # dont forget to calculate the overtime


    def save(self, *args, **kwargs):
        self.calculateArbeitszeit()
        super(Arbeitsstunden, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.mitarbeiter} - {self.datum} - {self.beginn} - {self.ende} - {self.status}'