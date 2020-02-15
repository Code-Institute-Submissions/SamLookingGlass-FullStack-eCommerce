def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # retrieve shopping cart
    # cart = request.session.get('shopping_cart', {})
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)
    
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
    
    #generate the stripe session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
        payment_intent_data={
            'capture_method':'manual'
        }
    )
    
    # render the template
    return render(request, '', {
        'session_id':session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
def checkout_success(request):
    user = request.user 
    cart = Cart.object.get(user=user)
    cart.delete()
    return render(request, '.html')
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")
    