from django.contrib import admin
from . import models


admin.site.regitser(models.Booking)
admin.site.register(models.Menu)