from django.contrib import admin
from .models import Mitarbeiter, Adresse, Arbeitsstunden



# Register your models here.
admin.site.register(Mitarbeiter)
admin.site.register(Adresse)
admin.site.register(Arbeitsstunden)