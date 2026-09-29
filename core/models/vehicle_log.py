from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .vehicles import Vehicle


class VehicleLog(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle_logs')
    pickup_time = models.DateTimeField(default=timezone.now)
    return_time = models.DateTimeField(null=True, blank=True)
    mileage = models.PositiveIntegerField()

    def __str__(self):
        return self.vehicle.plate_number if self.vehicle else str(self.id)

    def earning(self):
        return self.mileage*self.user.profile.rate
