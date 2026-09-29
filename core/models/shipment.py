from django.db import models
from django.conf import settings

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    dispatcher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="created_shipments")
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True, related_name="assigned_shipments")
    vehicle = models.ForeignKey("Vehicle", on_delete=models.SET_NULL, null=True,blank=True)
    estimated_distance = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

