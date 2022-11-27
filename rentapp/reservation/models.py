from django.db import models

from django.utils.timezone import now
from django.contrib.auth.models import User

from organization.models import Product


class Reservation(models.Model):
    """
    Define a Reservation.

    start_date,
    end_date,
    renter,
    product_rented,
    quantity_rented,
    is_reservation_executed,
    is_endof_reservation_executed

    """
    start_date = models.DateTimeField('Date', default=now)
    end_date = models.DateTimeField('Date', default=now)
    renter = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    product_rented = models.ForeignKey(Product,
                                       on_delete=models.CASCADE)
    quantity_rented = models.IntegerField('Quantity', default=1)
    is_reservation_executed =models.BooleanField('Is executed', default=False)
    is_endof_reservation_executed =models.BooleanField('End of reservation executed', default=False)
    

    def __str__(self):
        """
        """
        return 'Reservation of ' + self.quantity_rented.__str__() + " " + self.product_rented.__str__() + " by " + self.renter.__str__() + " from " + self.start_date.__str__() + ' to ' + self.end_date.__str__()


