from django.db import models

# Create your models here.

# Category (Fields on Admin Dashboard)
class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Products (Fields on Admin Dashboard)
# class Product(models.Model):
