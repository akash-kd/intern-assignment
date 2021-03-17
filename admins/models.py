from django.db import models

# Create your models here.
class Advisor(models.Model):
    advisor_name = models.TextField(max_length=200)
    advisor_url  = models.URLField()
