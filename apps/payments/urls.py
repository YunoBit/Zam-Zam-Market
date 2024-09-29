from rest_framework.routers import DefaultRouter
from apps.payments.views import TransactionViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
