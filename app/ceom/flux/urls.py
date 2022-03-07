
from django.urls import path
import ceom.flux.views


urlpatterns = [
    path('', ceom.flux.views.index),

    
]