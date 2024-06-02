from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PaymentFilter
    ordering_fields = ['date', 'sum']
    ordering = ['date']
