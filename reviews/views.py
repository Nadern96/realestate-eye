from django.shortcuts import render
from .forms import CompanyReviewForm
from django.contrib import messages #import messages
from django.utils.translation import gettext as _
from .models import CompanyReview

# Create your views here.

def review(request):
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

def list_reviews(request):
    reviews = CompanyReview.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews_list.html', context=context)
