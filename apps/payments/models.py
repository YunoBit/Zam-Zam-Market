from django.db import models
from apps.orders.models import Order

class Transaction(models.Model):
    order = models.OneToOneField(
        Order, 
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    status = models.CharField(
        max_length=50, 
        default='pending'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
