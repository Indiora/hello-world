from django.contrib import admin
from django.urls import path, include
from .views import HomeView, OfferView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('offer/', OfferView.as_view(), name='offer'),
]