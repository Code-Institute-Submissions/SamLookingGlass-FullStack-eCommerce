from django.db import models
from django.conf import settings
from pyuploadcare.dj.models import ImageField


# Category (Fields on Admin Dashboard)
class Category(models.Model):
    title = models.CharField(max_length=300, blank=True)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Products (Fields on Admin Dashboard)
class Product(models.Model):
    name = models.CharField(max_length=300, blank=True)
    price = models.FloatField(blank=True)
    product_photo = ImageField(blank=True, manual_crop="")
    slug = models.SlugField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    
    

    def __str__(self):
        return self.name