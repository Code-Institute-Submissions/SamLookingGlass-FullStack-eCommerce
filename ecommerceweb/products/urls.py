from django.urls import path
from django.contrib import messages
from . views import Home, ProductView

app_name= 'mainapp'

urlpatterns = [
    # Path for homepage
    path('', Home.as_view(), name='home'),
    # Path for product view
    path('product/<slug>', ProductView, name='ProductView')
]