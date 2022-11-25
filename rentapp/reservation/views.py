from rest_framework import viewsets

from .serializers import *
from .models import *

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

