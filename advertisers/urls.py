from django.urls import path

from . import views

urlpatterns = [
    path("", views.AdvertiserListView.as_view(), name="advertiser-list"),
    path("add/", views.AdvertiserCreateView.as_view(), name="advertiser-add"),
    path("<int:pk>/", views.AdvertiserUpdateView.as_view(), name="advertiser-update"),
]
