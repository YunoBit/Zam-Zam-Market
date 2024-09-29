from django.db import models
from apps.products.models import Product
from apps.users.models import User

class Order(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=50, 
        default='pending'
    )

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        related_name='items', 
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1
    )
