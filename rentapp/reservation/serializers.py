from rest_framework import serializers

from .models import *


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'start_date', 'end_date', 'renter', 'product_rented']
