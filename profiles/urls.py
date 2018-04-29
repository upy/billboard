from django.urls import path

from . import views

urlpatterns = [
    path("", views.RepresentativeListView.as_view(), name="representative-list"),
    path("me/", views.LoggedInRepresentativeUpdateView.as_view(), name="profile"),
    path("add/", views.RepresentativeCreateView.as_view(), name="representative-add"),
    path(
        "<int:pk>/",
        views.RepresentativeUpdateView.as_view(),
        name="representative-update",
    ),
]
