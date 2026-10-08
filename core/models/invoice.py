from django.db import models


class Invoice(models.Model):
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for Shipment {self.shipment.id}"
