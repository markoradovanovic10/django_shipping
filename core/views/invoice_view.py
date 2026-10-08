from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from core.models import Invoice


class InvoicePDFView(LoginRequiredMixin, View):
    def test_func(self):
        return self.request.user.profile.user_type in ["admin", "dispatcher"]
    def get(self, request, pk):
        invoice = get_object_or_404(
            Invoice.objects.select_related(
                "shipment__company",
                "shipment__pickup_location__country",
                "shipment__delivery_location__country",
            ),
            pk=pk,
        )

        html = get_template("invoice_pdf.html").render({
            "invoice": invoice,
            "shipment": invoice.shipment,
            "font_path": str(settings.BASE_DIR / "core" / "static" / "fonts" / "DejaVuSans.ttf"),
        })

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'inline; filename="faktura-{invoice.pk:06d}.pdf"'

        result = pisa.CreatePDF(html, dest=response, encoding="UTF-8")
        if result.err:
            return HttpResponse("Greška pri generisanju PDF-a.", status=500)
        return response