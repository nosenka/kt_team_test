from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('rates', views.RateViewSet.as_view(actions={'get': 'list'})),
    path('rates/<int:pk>', views.RateViewSet.as_view(actions={'get': 'retrieve'})),

    path('update_rates', views.UpdateRatesView.as_view())
]
