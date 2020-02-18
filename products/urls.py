from django.urls import path
from django.contrib import messages
from .views import Home, ProductView

from checkout.views import checkout_success,checkout_cancelled

app_name= 'mainapp'

urlpatterns = [
    # Path for homepage
    path('', Home.as_view(), name='home'),
    # Path for product view
    path('product/<slug>', ProductView, name='ProductView'),
    path('success', checkout_success, name='checkout-success'),
    # Path for checkout cancelled
    path('cancelled', checkout_cancelled, name='checkout-cancelled')
]