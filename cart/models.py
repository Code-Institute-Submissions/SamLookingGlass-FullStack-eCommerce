from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

# Getting the user model
User = get_user_model()

# Cart (Fields on Admin Dashboard)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Product, through='Cart_product_intermediary')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username 
        
# Intermediary Model
class Cart_product_intermediary(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Order (Fields on Admin Dashboard)
class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username 
    
    # Function to calculate total price and display it
    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
        
        return total

