from django_filters import rest_framework as filters
from .models import Payment


class PaymentFilter(filters.FilterSet):
    class Meta:
        model = Payment
        fields = {
            'date': ['exact', 'year__gt', 'year__lt', 'month', 'day', 'date__range'],
            'course': ['exact'],
            'lesson': ['exact'],
            'WayOfPay': ['exact'],
        }
