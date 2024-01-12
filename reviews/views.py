from django.shortcuts import render
from .forms import CompanyReviewForm
from django.contrib import messages #import messages
from django.utils.translation import gettext as _
from .models import CompanyReview
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html',)

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
    search_post = request.GET.get('search')
            
    if search_post:
        reviews = CompanyReview.objects.filter(Q(company_name__icontains=search_post))
    else:
        # If not searched, return default posts
        reviews = CompanyReview.objects.all()

    context = {
        'reviews': reviews,
        'search': search_post
    }
    return render(request, 'reviews_list.html', context=context)
