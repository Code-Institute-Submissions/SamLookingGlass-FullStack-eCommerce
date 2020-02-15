from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, Order, Cart_product_intermediary
from products.models import Product
from django.views.generic import ListView
from django.contrib import messages

# Function to Display items in cart
def CartView(request):
    user = request.user    
    print(user)

    print("ASD")
    try:
        carts = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        carts = Cart.objects.create(user=user)
    # orders = Order.objects.get(user=user) 
    order = None

    print(carts)
    return render(request, 'cart.html', {"carts": carts, 'order': order})
    

    # print(carts.orders)    
    # if carts.exists():
    #     if orders.exists():
    #         order = orders[0]
    #         return render(request, 'cart.html', {"carts": carts, 'order': order})
    #     else:
    #         messages.warning(request, "You do not have any item in your Cart")
    #         return redirect("mainapp:home")
		
    # else:
    #     messages.warning(request, "You do not have any item in your Cart")
    #     return redirect("mainapp:home")

# Function to add products to cart
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user    
    carts = Cart.objects.get(user=user)
    if request.method == "GET":
        
       
        if carts.item.all().filter(pk=item.id):
            cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,
            cart=carts)
            cart_product_intermediary.quantity += 1
            cart_product_intermediary.save()
        else:
            carts.item.add(
                item,
                through_defaults ={
                    'quantity':1,
                }
            )
        
    else:
        # request.POST.get('quantity')
        if carts.item.all().get(pk=item.id):
            cart_product_intermediary = Cart_product_intermediary.objects.get(product=item,
            cart=carts)
            #cart_product_intermediary.quantity +=request.POST.get('quantity')
            cart_product_intermediary.save()
        else:
            #carts.item.add(
           #     item,
           #     through_defaults ={
           #         'quantity':#request.POST.get('quantity'),
            #    }
        #    )   
            pass

    return redirect("mainapp:home")

     

    # order_item, created = Cart.objects.get_or_create(
    #     item=item,
    #     user=request.user
    # )
    # order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    # if order_qs.exists():
    #     order = order_qs[0]
    #     # Check if the product item is in the order
    #     if order.orderitems.filter(item__slug=item.slug).exists():
    #         # Calculates quantity in cart
    #         order_item.quantity += 1
    #         order_item.save()
    #         messages.info(request, f"{item.name} quantity has updated.")
    #         # if request.get_full_path == mainapp:home:
    #         return redirect("mainapp:home")
    #         # return
    #     else:
    #         order.orderitems.add(order_item)
    #         messages.info(request, "This item was added to your cart.")
    #         return redirect("mainapp:home")
    #         # return
    # else:
    #     order = Order.objects.create(
    #         user=request.user)
    #     order.orderitems.add(order_item)
    #     messages.info(request, "This item was added to your cart.")
    #     return redirect("mainapp:home")





# Function to remove product from cart (Buggy)
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        cart_qs.delete()
        # Checking the cart quantity
        # if cart.quantity > 1:
            # cart.quantity -= 1
            # cart_qs.delete()
            # cart.save()
        # else:
            # cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # Check if the product is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("cartapp:cart")
        else:
            # messages.info(request, "This item was not in your cart")
            return redirect("cartapp:cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("mainapp:home")

# Decrease the quantity of the cart 
def decreaseCart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} has removed from your cart.")
            messages.info(request, f"{item.name} quantity has updated.")
            return redirect("cartapp:cart")
        else:
            messages.info(request, f"{item.name} quantity has updated.")
            return redirect("cartapp:cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("mainapp:home")

# Increase the quantity of the cart 
def increaseCart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has updated.")
                return redirect("cartapp:cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("mainapp:home")

