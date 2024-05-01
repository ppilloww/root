from django.db import models
from django.utils import timezone

# Create your models here.

######################################### Database operations #########################################

class Adresse(models.Model):
    strasse = models.CharField(max_length=255)
    stadt = models.CharField(max_length=255)
    plz = models.CharField(max_length=10)
    land = models.CharField(max_length=50)
    hausnummer = models.IntegerField()

    def __str__(self):
        return f"{self.strasse} {self.hausnummer}, {self.plz} {self.stadt}, {self.land}"


# Model for Mitarbeiter
class Mitarbeiter(models.Model):
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    vorgesetzter = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    geburtsdatum = models.DateField()
    position = models.CharField(max_length=255, blank=True)
    gehalt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hr_tag = models.BooleanField(default=False)
    passwort = models.CharField(max_length=255)
    admin_tag = models.BooleanField(default=False)
    urlaubstage = models.IntegerField()
    wochenstundensatz = models.IntegerField()
    ueberstunden = models.DecimalField(max_digits=5, decimal_places=2, blank=-True, null=True)
    geschlecht = models.CharField(max_length=1, choices=[('M', 'Männlich'), ('F', 'Weiblich')])
    quartalueberstunden = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    jahresueberstunden = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def has_module_perms(self, app_label):
        return self.is_staff

    def get_username(self):
        return self.email

    def __str__(self):
        return f"{self.vorname} {self.nachname}"


class Abteilung(models.Model):
    abteilungsleiter = models.ForeignKey(Mitarbeiter, on_delete=models.SET_NULL, null=True, blank=True, related_name='geleitete_abteilungen')
    abteilungsname = models.CharField(max_length=255)

    def __str__(self):
        return self.abteilungsname


class Abteilungsleiter(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Arbeitsstunden(models.Model):
    mitarbeiter = models.ForeignKey(Mitarbeiter, on_delete=models.CASCADE, related_name='arbeitsstunden')
    datum = models.DateField()
    arbeitsbeginn = models.TimeField()
    arbeitsende = models.TimeField()
    pause = models.DecimalField(max_digits=4, decimal_places=2)
    gesamtarbeitszeit = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.mitarbeiter} Arbeitsstunden am {self.datum}"

class Urlaub(models.Model):
    mitarbeiter = models.ForeignKey(Mitarbeiter, on_delete=models.CASCADE, related_name='urlaube')
    startdatum = models.DateTimeField()
    enddatum = models.DateTimeField()
    genehmigt = models.BooleanField()
    antrag = models.BooleanField()

    def __str__(self):
        return f"{self.mitarbeiter} Urlaub von {self.startdatum} bis {self.enddatum}"
    




######################################### Database operations #########################################
