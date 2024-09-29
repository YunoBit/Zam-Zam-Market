from rest_framework.routers import DefaultRouter
from apps.orders.views import OrderViewSet, OrderItemViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
