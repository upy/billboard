from django.urls import path

from . import views

urlpatterns = [
    path('', views.RepresentativeListView.as_view(),
         name='representative-list'),
    path('me/', views.LoggedInRepresentativeUpdateView.as_view(),
         name='profile'),
    path('<int:pk>/', views.RepresentativeUpdateView.as_view(),
         name='representative-update'),
]
