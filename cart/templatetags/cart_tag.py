from django import template
from products.models import Product
from cart.models import Cart_product_intermediary
from flask import request

register = template.Library()

@register.filter
def cart_total(request):
    current_user = request
    current_user = str(current_user) 
    # Pull all objects from Cart_product_intermediary in database  
    carts = Cart_product_intermediary.objects.all()
    cart_items = []
    # Check if item(s) belongs to current logged in user
    for item in carts:
        user = str(item.cart)
        # if item belongs to user, append to cart_items
        if user == current_user:
            cart_items.append(user)      
    if carts:
    	    return len(cart_items)
    else:
    	return 0