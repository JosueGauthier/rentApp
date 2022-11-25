from django.db import models

from django.utils.timezone import now
from django.contrib.auth.models import User

from organization.models import Product


class Reservation(models.Model):
    """
    Define a Reservation.

    """
    start_date = models.DateTimeField('Date', default=now)
    end_date = models.DateTimeField('Date', default=now)
    renter = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    renter = models.ForeignKey(Product,
                               on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the display name of the Sale.

        :returns: pk of sale
        :rtype: string
        """
        return 'Achat ' + self.shop.__str__() + ', ' + self.string_products()
