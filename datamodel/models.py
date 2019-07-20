from django.db import models

# Create your models here.


class Datamodel(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()
    address = models.TextField()
