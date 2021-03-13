from django.contrib import admin

# Register your models here.
# username = hr || password = 123
from .models import contactUs
#

admin.site.register(contactUs)