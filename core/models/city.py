from django.db import models
from .country import Country
from core.services.DistanceService import DistanceService
import requests

class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.country.name}"

    def update_coords(self):
        longitude, latitude = DistanceService().get_coords_by_name(f"{self.name}, {self.country.name}")
        self.latitude = latitude
        self.longitude = longitude
        return True

    def save(self, *args, **kwargs):
        self.update_coords()
        super().save(*args, **kwargs)