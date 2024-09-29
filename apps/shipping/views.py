from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from apps.shipping.models import ShippingZone
from apps.shipping.serializers import ShippingZoneSerializer

class ShippingZoneViewSet(viewsets.ModelViewSet):
    queryset = ShippingZone.objects.all()
    serializer_class = ShippingZoneSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
