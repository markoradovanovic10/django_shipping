from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from ..models import Invoice

class InvoiceListView(UserPassesTestMixin, ListView):
    model = Invoice
    template_name = 'inovice_list.html'
    context_object_name = 'invoices'

    def test_func(self):
        return self.request.user.profile.user_type in ['admin', 'dispatcher']