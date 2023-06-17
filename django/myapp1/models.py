from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=122)

    phone = models.CharField(max_length=122)
    city = models.CharField(max_length=122)