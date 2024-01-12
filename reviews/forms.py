from django import forms
from .models import CompanyReview
from django.utils.translation import gettext as _


class CompanyReviewForm(forms.Form):
    company_name = forms.CharField(
        required=True, max_length=256, label=_('Company name'))
    company_website = forms.CharField(
        required=False, max_length=256, label=_('Company website'))
    company_facebook = forms.CharField(
        required=False, max_length=256, label=_('Company facebook'))
    complaint_reason = forms.ChoiceField(
        required=True, choices=CompanyReview.COMPLAINT_REASON_CHOICES, label=_('Complaint reason'))
    # client_phone_number = forms.CharField(
    #     required=False, max_length=256, label=_('Phone Number'))
    gov = forms.ChoiceField(
        required=True, choices=CompanyReview.GOV_CHOICES, label=_('Governorate'), help_text=_('apartment Governorate'))
    region = forms.CharField(
        required=True, max_length=256, label=_('Region'), help_text=_('apartment region'))
    neighborhood = forms.CharField(
        required=True,  max_length=256, label=_('Neighborhood'), help_text=_('apartment neighborhood'))
    comment = forms.CharField(required=True,widget=forms.Textarea, label=_('Comment'), help_text=_('details'))
