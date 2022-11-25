from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import *
from .models import *

class ReservationViewSet(viewsets.ModelViewSet):
    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'start_date', 'end_date', 'renter', 'product_rented']

