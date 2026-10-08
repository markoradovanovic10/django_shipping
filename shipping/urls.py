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
from core.views import InvoicePDFView
from django.contrib.auth import views as auth_views
from core.views import HomePageView
from core.views import InvoiceListView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/login.html', next_page='home_page'), name='login'),
    path('admin/', admin_site.urls),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dispatch/', DispatchView.as_view(), name='dispatch'),
    path('shipment/<int:pk>/edit/', ShipmentUpdateView.as_view(), name='shipment_edit'),
    path('invoice/<int:pk>/view', InvoicePDFView.as_view(), name='invoice'),
    path('general/', HomePageView, name='home_page'),
    path('invoices/', InvoiceListView.as_view(), name='invoice_list' )
]
