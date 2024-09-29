from django.db import models

from apps.categories.models import Category

class Product(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product'
    )


    def __str__(self):
        return self.title


class ProductImage(models.Model):
    blog = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL, 
        blank=True,
        null=True, 
        related_name='product_name'
    )
    photo = models.ImageField(
        upload_to='products'
    )


    def __str__(self):
        return self.blog.title