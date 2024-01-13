from django.db import models

# Create your models here.


class booking(models.Model):
    id = models.IntegerField(max_length=11, primary_key= True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    boooking_date = models.DateField()


class MenuItem(models.Model):
    id = models.IntegerField(max_length=5,primary_key= True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.DateField()

