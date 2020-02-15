from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, Order, Cart_product_intermediary
from products.models import Product
from django.views.generic import ListView
from django.contrib import messages

# Function to Display items in cart
def CartView(request):
    # Get user info from database
    user = request.user    
    try:
        carts = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        carts = Cart.objects.create(user=user)
    order = None
    return render(request, 'cart.html', {"carts": carts, 'order': order})

# Function to add products to cart
def add_to_cart(request, slug):
    source_url = request.META.get('HTTP_REFERER')
    item = get_object_or_404(Product, slug=slug)
    user = request.user    
    carts = Cart.objects.get(user=user)
    # Check if method is GET, if yes do this (User added from home page/cart page):
    if request.method == "GET":
        # Check if item exists in cart, if it exists, increase quantity in cart
        if carts.item.all().filter(pk=item.id):
            cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,
            cart=carts)
            cart_product_intermediary.quantity += 1
            cart_product_intermediary.save()
            messages.info(request, f"{item.name} quantity has been updated in cart.")
            if source_url[-5:] == 'cart/':
                return redirect("cartapp:cart")    
            return redirect("mainapp:home")   
        # If item does not exist in cart, add to cart.
        else:
            carts.item.add(
                item,
                through_defaults ={
                    'quantity':1,
                }
            )
            messages.info(request, "This item was added to your cart.")
            return redirect("mainapp:home")    
    # Check if method is not GET (i.e. POST), do this (User added from product info page):
    else:
        # Get user defined quantity from POST method
        user_quantity = int(request.POST.get('quantity'))
        # Check if item exists in cart, if yes, do this:
        if carts.item.all().filter(pk=item.id):
            cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,
            cart=carts)
            cart_product_intermediary.quantity += user_quantity
            cart_product_intermediary.save()
            messages.info(request, f"{item.name} quantity has been updated in cart.")
            return redirect("mainapp:ProductView", slug=item.slug)
        # If item does not exists in cart, do this:
        else:
            carts.item.add(
                item,
                through_defaults ={
                    'quantity':1,
                }
            )
            messages.info(request, "This item was added to your cart.")    
    return redirect("mainapp:ProductView", slug=item.slug)

# Function to remove product from cart (Buggy)
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user    
    carts = Cart.objects.get(user=user)
   # Check if item exists in cart, if it exists, it will delete from cart
    if carts.item.all().filter(pk=item.id):
        # Filters out the exact product
        cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,
        cart=carts)
        cart_product_intermediary.delete()
        messages.warning(request, f"{item.name} has removed from your cart.")   
        return redirect("cartapp:cart")
    # Check if item exists in cart, if not:
    else:
        messages.warning(request, "The item does not exists in the cart.")   
        return redirect("cartapp:cart")


# Function to decrease quantity to cart
def decreaseCart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user    
    carts = Cart.objects.get(user=user)
    
    # Check if item exists in cart, if it exists, decrease quantity in cart
    if carts.item.all().filter(pk=item.id):
        # Filters out the exact product
        cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,
        cart=carts)
        if cart_product_intermediary.quantity > 1:
            cart_product_intermediary.quantity -= 1
            cart_product_intermediary.save()
            messages.info(request, f"{item.name} quantity has been updated.")
            return redirect("cartapp:cart")
        else:
            cart_product_intermediary.delete()
            messages.warning(request, f"{item.name} has removed from your cart.")   
            return redirect("cartapp:cart")
