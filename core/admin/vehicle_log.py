from django.contrib import admin
from ..models import VehicleLog

class VehicleLogInline(admin.StackedInline):
    model = VehicleLog
    extra = 1

    exclude = ['vehicle']


    def has_change_permission(self, request, obj=None):
        return False
