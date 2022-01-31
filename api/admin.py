from django.contrib import admin

# Register your models here.

from .models import MetamaskUser

admin.site.register(MetamaskUser)