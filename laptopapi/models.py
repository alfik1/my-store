from django.db import models

# Create your models here.
class Laptops(models.Model):

    name=models.CharField(max_length=120)
    brand=models.CharField(max_length=120)
    screen_size=models.IntegerField()
    cpu=models.CharField(max_length=50)
    ram=models.CharField(max_length=60)
    price=models.PositiveIntegerField()
    ratings = models.FloatField(null=True, default=3)



