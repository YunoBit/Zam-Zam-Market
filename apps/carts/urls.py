from rest_framework.routers import DefaultRouter
from apps.carts.views import CartViewSet, CartItemViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
