from django.utils.timezone import localtime
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *

# Define global timer to avoid too many requests
#
"""
from threading import Timer
# duration is in seconds
t = Timer(20 * 60)
t.start()
# wait for time completion
t.join()
can checkReservationTimer =  """


class ReservationViewSet(viewsets.ModelViewSet):

    def dispatch(self, request, *args, **kwargs):
        check_reservation_for_non_consumable()
        self.update
        return super().dispatch(request, *args, **kwargs)

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'start_date',
                        'end_date', 'renter', 'product_rented']

    def create(self, request):
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            data = dict(serializer.validated_data)
            product = Product.objects.get(id=data['product_rented'].id)

            if product.is_consumable == True:
                isReservationSuccess = reservation_for_consumable(
                    product, data['quantity_rented'])
                serializer.save()
                if isReservationSuccess == True:
                    return Response({"Sucess": serializer.data}, status=status.HTTP_201_CREATED)
                else:
                    return Response("Error no reservation create : Quantity not available", status=status.HTTP_400_BAD_REQUEST)

            # if the product is not a consumable
            else:
                # we create a list of the reservation of the same product and the reservation is not finished
                reservation_list = Reservation.objects.filter(
                    product_rented=product.id, is_endof_reservation_executed=False)

                # if there is no reservation we just create the reservation
                if len(reservation_list) == 0:
                    if data['quantity_rented'] <= product.qty_total:
                        serializer.save()
                        return Response("Success",
                                        status=status.HTTP_201_CREATED)
                    else:
                        return Response("Error No reservation create : Quantity not available",
                                        status=status.HTTP_400_BAD_REQUEST)

                # if there is a reservation we check if the date is available
                else:
                    for j in range(0, len(reservation_list)):
                        if data['start_date'] <= reservation_list[j].end_date and data['start_date'] >= reservation_list[j].start_date:
                            return Response("Error No reservation created : Date non available", status=status.HTTP_406_NOT_ACCEPTABLE)
                        if data['end_date'] >= reservation_list[j].start_date and data['end_date'] <= reservation_list[j].end_date:
                            return Response("Error No reservation created : Date non available", status=status.HTTP_406_NOT_ACCEPTABLE)

                    serializer.save()
                    check_reservation_for_non_consumable()
                    return Response("Success", status=status.HTTP_201_CREATED)

        return Response("Error No reservation create. An error has occurred", status=status.HTTP_400_BAD_REQUEST)


def reservation_for_consumable(product, qty_rented):
    product.qty_available = product.qty_available - qty_rented

    if product.qty_available >= 0:
        product.save()
        return True
    else:
        return False


def check_reservation_for_non_consumable():

    reservationList = Reservation.objects.filter(
        is_endof_reservation_executed=False)
    for i in range(len(reservationList)):
        reservation = Reservation.objects.get(id=reservationList[i].id)
        product = Product.objects.get(id=reservation.product_rented.id)
        time_now = localtime()

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
                    # if for a reason the renting process was not started we start here
                    if reservation.is_reservation_executed == False:
                        print("Start renting : "+product.name_product)
                        product.qty_available = product.qty_available - reservation.quantity_rented
                        product.save()
                        reservation.is_reservation_executed = True
                        reservation.save()

                    # And then we stop it
                    print("Stop renting : "+product.name_product)
                    product.qty_available = product.qty_available + reservation.quantity_rented

                    # We check that the product.qty_available is not > product.qty_total
                    if product.qty_available > product.qty_total:
                        product.qty_available = product.qty_total

                    product.save()
                    reservation.is_endof_reservation_executed = True
                    reservation.save()
