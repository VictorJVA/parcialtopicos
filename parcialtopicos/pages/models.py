from django.db import models

# Create your models here.
class Flight(models.Model):
    #id autoincrementable
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type
    type = models.CharField(max_length=100)
    price = models.FloatField()