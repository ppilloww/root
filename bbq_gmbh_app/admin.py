from django.contrib import admin
from bbq_gmbh_app.models import CustomUser, Address



# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Address)