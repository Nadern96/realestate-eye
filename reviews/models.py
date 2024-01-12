from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class CompanyReview(models.Model):
    COMPLAINT_REASON_CHOICES = [
        ("DL",  _("Delay")),
        ("RPI", _("Request Price Increase")),
        ("OT", _("Other"))
    ]

    GOV_CHOICES = [
        ("CA", _("Cairo")),
        ("GI", _("Giza")),
        ("OT", _("Other"))
    ]

    company_name = models.CharField(blank=False, null=False, max_length=256)
    company_website = models.CharField(blank=True, null=True, max_length=256)
    company_facebook = models.CharField(blank=True, null=True, max_length=256)
    complaint_reason = models.CharField(
        blank=False, null=False, choices=COMPLAINT_REASON_CHOICES, max_length=5)
    client_phone_number = models.CharField(
        blank=True, null=True, max_length=15)
    gov = models.CharField(blank=False, null=False,
                           choices=GOV_CHOICES, max_length=10)
    region = models.CharField(blank=False, null=False, max_length=256)
    neighborhood = models.CharField(blank=False, null=False, max_length=256)
    land_num = models.CharField(blank=True, null=True, max_length=20)
    comment = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def complaint_reason_verbose(self):
        return dict(CompanyReview.COMPLAINT_REASON_CHOICES)[self.complaint_reason]

    def gov_verbose(self):
        return dict(CompanyReview.GOV_CHOICES)[self.gov]