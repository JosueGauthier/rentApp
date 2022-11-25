from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from .views import UserViewSet

from organization.urls import organization_patterns
from reservation.urls import reservation_patterns



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('', include(organization_patterns)),
    path('', include(reservation_patterns)),
]
