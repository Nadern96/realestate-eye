from django.shortcuts import render
from .forms import CompanyReviewForm
from django.contrib import messages #import messages
from django.utils.translation import gettext as _


# Create your views here.
from .models import CompanyReview
def index(request):
    if request.method == 'POST':
        form = CompanyReviewForm(request.POST)
        if form.is_valid():
            # Process the forms
            CompanyReview.objects.create(**form.cleaned_data)
            messages.success(request, _('Your data submitted Succefully'))

    form = CompanyReviewForm()
    context = {
        'form': form
    }
    return render(request, 'review_form.html', context=context)