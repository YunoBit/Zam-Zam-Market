from rest_framework.routers import DefaultRouter
from apps.shipping.views import ShippingZoneViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'shipping-zones', ShippingZoneViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
