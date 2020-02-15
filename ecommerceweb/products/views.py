
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from products.models import Product
from cart.models import Cart, Order
from django.contrib import messages


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

# Function to add order to cart on product view
def variable_add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    quantity_selected = request.GET.get('quantity')
    if request.method == 'GET':
        if order_qs.exists():
            order = order_qs[0]
            # Check if the product item is in the order
            if order.orderitems.filter(item__slug=item.slug).exists():
                # Calculates quantity in cart
                order_item.quantity = order_item.quantity + quantity_selected
                order_item.save()
                messages.info(request, f"{item.name} quantity has updated.")
                # if request.get_full_path == mainapp:home:
                return redirect("mainapp:ProductView")
                # return
            else:
                order.orderitems = quantity_selected
                order_item.save()
                messages.info(request, "This item was added to your cart.")
                return redirect("mainapp:ProductView")
                # return
        else:
            order = Order.objects.create(
                user=request.user)
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("mainapp:ProductView")
    else:
        return redirect("mainapp:ProductView")