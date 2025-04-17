from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    amount= models.BigIntegerField()
    owner= models.ForeignKey(User, on_delete= models.PROTECT, related_name= "the_owner_of_the_wallet")