from django.urls import path, include
from .views import CartView, add_to_cart, remove_from_cart, decreaseCart
from products.views import Home

app_name= 'cartapp'

urlpatterns = [
    # Path for cartview
    path('', CartView, name='cart'),

]