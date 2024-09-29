from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.payments.models import Transaction
from apps.payments.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
