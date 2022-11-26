from rest_framework import routers
from django.contrib import admin
from django.urls import path, include


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import UserViewSet

from organization.urls import organization_patterns
from reservation.urls import reservation_patterns


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include(router.urls)),
    path('', include(organization_patterns)),
    path('', include(reservation_patterns)),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    # get a new token before the old expires.
    path('api/token/refresh/', TokenRefreshView.as_view, name='token_refresh'),
    
    path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'),

]
