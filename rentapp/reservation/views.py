from django.utils.timezone import now
import sys
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import *
from .models import *

from rest_framework.response import Response
from rest_framework import status


class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'start_date',
                        'end_date', 'renter', 'product_rented']

    def create(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # reservation_process(serializer.data)

            return Response({"Sucess": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return Response({"Sucess": "Reservation made"}, status=status.HTTP_201_CREATED)


def reservation_for_consumable(data):
    product = Product.objects.get(id=data['product_rented'])
    print(product.name_product)
    product.qty_available = product.qty_available - data['quantity_rented']
    product.save()


def reservation_for_non_consumable():

    for i in range(1, Reservation.objects.count()+1):
        reservation = Reservation.objects.get(id=i)
        product = Product.objects.get(id=reservation.product_rented)
        time_now = now()

        if product.is_consumable == False:

            if time_now > reservation.start_date and time_now < reservation.end_date:
                if reservation.is_reservation_executed == False:
                    print("Start renting : "+product.name_product)
                    product.qty_available = product.qty_available - reservation.quantity_rented
                    product.save()
                    reservation.is_reservation_executed = True

            if time_now > reservation.end_date:
                if reservation.is_endof_reservation_executed == False:
                    print("Stop renting : "+product.name_product)
                    product.qty_available = product.qty_available + reservation.quantity_rented
                    product.save()
                    reservation.is_endof_reservation_executed = True

    # if product.is_consumable == False:

    """ product.qty_available = product.qty_available - data['quantity_rented']
        
    product.save()
     """
