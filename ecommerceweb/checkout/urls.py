from django.urls import path
from .views import checkout, checkout_success, checkout_cancelled

app_name= 'checkoutapp'

urlpatterns = [
    # Path for checkout
    path('', checkout, name='checkout'),
]
