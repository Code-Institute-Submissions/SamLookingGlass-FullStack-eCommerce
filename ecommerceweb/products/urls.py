from django.urls import path
from django.contrib import messages
from . views import Home, ProductView, variable_add_to_cart

app_name= 'mainapp'

urlpatterns = [
    # Path for homepage
    path('', Home.as_view(), name='home'),
    # Path for product view
    path('product/<slug>', ProductView, name='ProductView'),
    # Path for variable add to cart
    path('product/<slug>/add', variable_add_to_cart, name='variable_add_to_cart'),
]