from django.db import models

# Create your models here.


class Datamodel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
