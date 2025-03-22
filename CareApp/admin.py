from django.contrib import admin

# Register your models here.

from .models import RegistrationDB
# from django.contrib.auth.models import User


admin.site.register(RegistrationDB)
# admin.site.register(User)

