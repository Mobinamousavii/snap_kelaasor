from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
class Wallet(models.Model):
    amount= models.BigIntegerField(default= 1000000)
    owner= models.ForeignKey(User, on_delete= models.PROTECT, related_name= "the_owner_of_the_wallet")

class Trip(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    origin_latitude = models.CharField(max_length=100)
    origin_longitude = models.CharField(max_length=100)
    destination_latitude= models.CharField(max_length=100)
    destinatio_longitude = models.CharField(max_length=100)
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)

