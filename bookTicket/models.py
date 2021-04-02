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
    bookedSeat = models.CharField(max_length=100)
    time1 = models.TimeField()
    time2 = models.TimeField()

    def __str__(self):
        return self.arrival+' --> '+self.destination

class ticketDetail(models.Model):
    ticketID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    busID = models.IntegerField()
    journeyDate = models.DateField()
    totalFare = models.IntegerField(default=0)
    seatNo = models.CharField(max_length=2)
    passName = models.CharField(max_length=50)
    passAge = models.IntegerField()
    PassGender = models.CharField(max_length=7)

    def __str__(self):
        return self.passName