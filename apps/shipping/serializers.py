from rest_framework import serializers
from apps.shipping.models import ShippingZone

class ShippingZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingZone
        fields = '__all__'
