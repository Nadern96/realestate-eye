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
    search_by = request.GET.get('search_by')
    gov = request.GET.get('gov')
    complain_reason = request.GET.get('complain_reason')

    search_post = request.GET.get('search')

    query = []

    if gov is not None:
        query.append(Q(gov=gov))
    
    if complain_reason is not None:
        query.append(Q(complaint_reason=complain_reason))

    if search_post is not None and len(search_post) > 0:
        if search_by == "company_name":
            query.append(Q(company_name__icontains=search_post))

        elif search_by == "region":
            query.append(Q(region__icontains=search_post))

        elif search_by == "neighborhood":
            query.append(Q(neighborhood__icontains=search_post))

    if len(query):
        reviews = CompanyReview.objects.filter(*query)
    else:
        # If not searched, return default posts
        reviews = CompanyReview.objects.all().order_by("-created_at")

    context = {
        'reviews': reviews,
        'search_by': search_by if search_by else '',
        'search': search_post if search_post else '',
        'complaint_reasons': list(CompanyReview.COMPLAINT_REASON_CHOICES),
        'govs': list(CompanyReview.GOV_CHOICES),
    }
    return render(request, 'reviews_list.html', context=context)
