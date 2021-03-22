from django.db import models

# Create your models here.
from datetime import date
# 

class busDetails(models.Model):
    busID = models.AutoField(primary_key=True)
    arrival = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    rent = models.IntegerField()
    distance = models.IntegerField()
    journeyDate = models.DateField(default=date.today)
    bookedSeat = models.CharField(max_length=50)
    time1 = models.TimeField()
    time2 = models.TimeField()

    def __str__(self):
        return self.arrival+' --> '+self.destination