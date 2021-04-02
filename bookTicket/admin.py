from django.contrib import admin

# Register your models here.
from .models import busDetails
from .models import ticketDetail
#

admin.site.register(busDetails)
admin.site.register(ticketDetail)