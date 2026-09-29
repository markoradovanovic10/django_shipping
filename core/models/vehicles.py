from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = (
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('van', 'Van'),
    )
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
        ('inactive', 'Inactive'),
    )

    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    plate_number = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    mileage = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    workhours = models.PositiveBigIntegerField(default=0)
    capacity = models.FloatField(default=0, help_text='Capacity in kg')

    def __str__(self):
        return f"{self.plate_number} ({self.vehicle_type})"


