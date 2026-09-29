from django.db import models
from .city import City

class Company(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='companies')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
