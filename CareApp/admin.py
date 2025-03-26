from django.contrib import admin

# Register your models here.

from .models import RegistrationDB
from CareApp.models import Payment
# from django.contrib.auth.models import User


admin.site.register(RegistrationDB)
admin.site.register(Payment)

# admin.site.register(User)

