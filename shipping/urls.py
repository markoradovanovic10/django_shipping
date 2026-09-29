"""
URL configuration for shipping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import ProfileView
from core.views import DispatchView
from core.admin import admin_site
from core.views import ShipmentUpdateView

urlpatterns = [
    path('admin/', admin_site.urls),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dispatch/', DispatchView.as_view(), name='dispatch'),
    path('shipment/<int:pk>/edit/', ShipmentUpdateView.as_view(), name='shipment_edit')
]
