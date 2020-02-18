from django.contrib import admin
from .models import Cart, Order,Cart_product_intermediary

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Cart_product_intermediary)