
from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from core.services.DistanceService import DistanceService
from ..models import Profile, Vehicle
from decimal import Decimal


class Shipment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CANCELLED = 'cancelled', 'Cancelled'
        ENROUTE = 'enroute', 'Enroute'
        DELIVERED = 'delivered', 'Delivered'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="shipments")
    pickup_location = models.ForeignKey("City", on_delete=models.CASCADE, related_name="pickup_shipments")
    delivery_location = models.ForeignKey("City", on_delete=models.CASCADE, related_name="delivery_shipments")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    dispatcher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="created_shipments")
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True, related_name="assigned_shipments")
    vehicle = models.ForeignKey("Vehicle", on_delete=models.SET_NULL, null=True,blank=True)
    estimated_distance = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def update_price(self):
        city_ori = [float(self.pickup_location.longitude), float(self.pickup_location.latitude)]
        city_dest = [float(self.delivery_location.longitude), float(self.delivery_location.latitude)]
        distance = DistanceService().get_distance(city_ori, city_dest)
        distance_km = distance[0][1]/1000
        self.estimated_distance = round(distance_km, 2)

        if self.driver:
            rate = Profile.objects.get(user=self.driver).rate
            self.price = Decimal(str(distance_km))*rate

        if self.vehicle:
            self.vehicle.mileage += distance_km
            self.vehicle.save(update_fields=['mileage'])
        return True

    def save(self, *args, **kwargs):
        self.update_price()
        super().save(*args, **kwargs)


