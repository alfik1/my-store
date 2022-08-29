from django.db import models
from django.db.models import Model

# Create your models here.

class Cars(Model):
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=50)
    fuel_capacity=models.PositiveIntegerField()
    top_speed=models.PositiveIntegerField()
    mileage=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    rating=models.FloatField(null=True,default=3)

