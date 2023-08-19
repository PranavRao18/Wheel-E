from django.db import models

class Offers(models.Model):
    is_active = models.BooleanField(default=True)
    distance = models.FloatField()
    fromCoordinatesLat = models.DecimalField(max_digits=9, decimal_places=6)
    fromCoordinatesLong = models.DecimalField(max_digits=9, decimal_places=6)
    request_id = models.CharField(max_length=100, unique=True,null = True)
    final_price = models.CharField(max_length=10,blank=True,null=True)
    is_accepted = models.BooleanField(default=False)
    driver_id = models.CharField(blank=True,null=True,max_length=50)
    user_id = models.CharField(blank=True,null=True,max_length=50)