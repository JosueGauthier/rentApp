from rest_framework import routers
from django.urls import path, include

from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'reservation',ReservationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
reservation_patterns = [
    path('', include(router.urls)),
    
]
