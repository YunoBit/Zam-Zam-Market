from rest_framework import serializers
from apps.carts.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(
        many=True
        )

    class Meta:
        model = Cart
        fields = '__all__'
