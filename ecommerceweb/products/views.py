from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from products.models import Product

# Displays html template
class Home(ListView):
    model = Product
    template_name = 'products/home.html'
