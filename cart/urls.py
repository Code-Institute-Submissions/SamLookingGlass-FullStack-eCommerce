from django.urls import path, include
from .views import CartView, add_to_cart, remove_from_cart, decreaseCart
from products.views import Home

app_name= 'cartapp'

urlpatterns = [
    # Path for cartview
    path('', CartView, name='cart'),
    # Path for decreasecart
    path('decrease/<slug>', decreaseCart, name='decrease-cart'),  
    # Path for add_to_cart
    path('add/<slug>', add_to_cart, name='add-cart'),
    # Path for remove_from_cart
    path('remove/<slug>', remove_from_cart, name='remove-cart'),

]