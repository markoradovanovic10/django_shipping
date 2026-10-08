from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Shipment, Invoice

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_type='driver')

@receiver(post_save, sender=Shipment)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        Invoice.objects.create(shipment=instance, price=instance.price, date=instance.created_at.date())


