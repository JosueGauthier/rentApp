from django.utils.timezone import now
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *


class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'start_date',
                        'end_date', 'renter', 'product_rented']

    def create(self, request):
        serializer = ReservationSerializer(data=request.data)
        
        if serializer.is_valid():
            
            product = Product.objects.get(id=serializer.data['product_rented'])
            if product.is_consumable == True:
                
                reservation_for_consumable(
                    product, serializer.data['quantity_rented'])
                serializer.save()
                return Response({"Sucess": serializer.data}, status=status.HTTP_201_CREATED)
            
            else:
                print("a1")
                reservation_list = Reservation.objects.filter(
                    product_rented=product.id)
                if len(reservation_list) == 0:
                    if serializer.data['quantity_rented'] < product.qty_total:
                        serializer.save()
                        Response({"Success": serializer.data}, status=status.HTTP_201_CREATED)
                    
                else:
                    
                    for j in reservation_list:
                        if serializer.data['start_date'] < reservation_list[j].end_date and serializer.data['start_date'] > reservation_list[j].start_date:
                            return Response({"Error No reservation created": serializer.data}, status=status.HTTP_406_NOT_ACCEPTABLE)
                        if serializer.data['end_date'] > reservation_list[j].start_date and serializer.data['end_date'] < reservation_list[j].end_date:
                             return Response({"Error No reservation created": serializer.data}, status=status.HTTP_406_NOT_ACCEPTABLE)       

                    serializer.save()
                    check_reservation_for_non_consumable()
                    return Response({"Success": serializer.data}, status=status.HTTP_201_CREATED)
                
        return Response({"Error No reservation create": serializer.data}, status=status.HTTP_400_BAD_REQUEST)


def reservation_for_consumable(product, qty_rented):
    print(product.name_product)
    product.qty_available = product.qty_available - qty_rented
    product.save()


def check_reservation_for_non_consumable():

    for i in range(1, Reservation.objects.count()+1):
        reservation = Reservation.objects.get(id=i)
        product = Product.objects.get(id=reservation.product_rented.id)
        time_now = now()

        if product.is_consumable == False:
            if time_now > reservation.start_date and time_now < reservation.end_date:
                if reservation.is_reservation_executed == False:
                    print("Start renting : "+product.name_product)
                    product.qty_available = product.qty_available - reservation.quantity_rented
                    product.save()
                    reservation.is_reservation_executed = True
                    reservation.save()

            if time_now > reservation.end_date:
                if reservation.is_endof_reservation_executed == False:
                    print("Stop renting : "+product.name_product)
                    product.qty_available = product.qty_available + reservation.quantity_rented
                    product.save()
                    reservation.is_endof_reservation_executed = True
                    reservation.save()

