from django.db import models

# Create your models here.


class Fileupload(models.Model):
    filename = models.CharField(max_length=50)
    date_uploaded = models.DateTimeField(auto_now=True)
