from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from products.models import Product

# Displays html template
class Home(ListView):
    model = Product
    template_name = 'home.html'

# Function to display product view
def ProductView(request, slug):
    results = Product.objects.get(slug=slug)
    context = {
        'product' : results
    }
    return render(request, "product_detail.html", context)

