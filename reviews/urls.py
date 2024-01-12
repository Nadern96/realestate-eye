from django.urls import path

from . import views

urlpatterns = [
    path("", views.review, name="review"),
    path("list", views.list_reviews, name="list_reviews"),
]