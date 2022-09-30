from django.urls import path
from .views import Metering

urlpatterns = [
    path('metering', Metering.as_view())
]