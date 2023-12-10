from django.db import models
from django.urls import reverse

# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=33)
    illiness = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    contact = models.BigIntegerField()


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    designation = models.CharField(max_length=100)
    specialist = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    def get_absolute_url(self):
        return reverse('doctorlist')




