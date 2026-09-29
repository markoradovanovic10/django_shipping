from django.contrib import admin
from ..models import City, Country

class CityInline(admin.StackedInline):
    model = City.country
    max_num = 1