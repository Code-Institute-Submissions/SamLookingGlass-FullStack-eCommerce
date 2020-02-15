from django.shortcuts import render, redirect, get_object_or_404,HttpResponse, reverse
from django.conf import settings
import env
import os
import stripe
from cart.models import Cart, Cart_product_intermediary
from products.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def checkout(request):
    user = request.user
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    
    # retrieve shopping cart
    # cart = request.session.get('shopping_cart', {})
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return redirect("cartapp:cart")
    
    line_items = []
    
    # generate the line_items
    for item in cart.item.all():
        # For each item in the cart, get its details from the database
        product = get_object_or_404(Product, pk=item.id)
        cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,cart=cart)
        line_items.append({
            'name': product.name,
            'amount': int(product.price*100), #convert to cents, in integer
            'currency':'sgd',
            'quantity':cart_product_intermediary.quantity
        })
    
    # reverse('mainapp:home')
    #generate the stripe session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse('mainapp:checkout-success')),
        cancel_url=request.build_absolute_uri(reverse('mainapp:checkout-cancelled')),
        payment_intent_data={
            'capture_method':'manual'
        }
    )
    
    # render the template
    return render(request, 'checkout.html', {
        'session_id':session.id,
        'public_key': os.environ.get('STRIPE_PUBLISHABLE_KEY')
    })
    
def checkout_success(request):
    user = request.user 
    cart = Cart.objects.get(user=user)
    cart.delete()
    return HttpResponse('Checkout success')
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")
    