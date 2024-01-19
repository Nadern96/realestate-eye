from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import CompanyReview

@receiver(pre_delete, sender=CompanyReview)
def delete_company_review(sender, instance, **kwargs):
    raise Exception('CompanyReview cant be deleted')