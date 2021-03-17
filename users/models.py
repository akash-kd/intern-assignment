from django.db import models
from admins.models import Advisor
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Booking(models.Model):
    time = models.DateTimeField(default = datetime.datetime.now)
    username = models.CharField(max_length=200)
    userid = models.IntegerField()
    advisorname = models.CharField(max_length=200)
    advisorid = models.IntegerField()

