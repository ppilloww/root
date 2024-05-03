from django.contrib import admin
from .models import Adresse, Mitarbeiter, Abteilung, Arbeitsstunden, Urlaub, Abteilungsleiter #migration Database
# Register your models here.


######################################### Database operations #########################################
 
admin.site.register(Adresse)
admin.site.register(Mitarbeiter)
admin.site.register(Abteilung)
admin.site.register(Abteilungsleiter)
admin.site.register(Arbeitsstunden)
admin.site.register(Urlaub)

######################################### Database operations #########################################