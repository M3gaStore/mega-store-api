from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=150)
    state = models.CharField(max_length=30)
    number = models.CharField()
    neighborhood = models.CharField(max_length=60)
    zip_code = models.CharField()
