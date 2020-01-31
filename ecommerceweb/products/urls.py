from django.urls import path
from . views import Home
from cart.views import add_to_cart, remove_from_cart
from products.views import Home
app_name= 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # Adding new paths for cart
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]