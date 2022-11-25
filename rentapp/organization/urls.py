from rest_framework import routers
from django.urls import path, include

from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'category', CategoryViewSet )
router.register(r'product', ProductViewSet )



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
organization_patterns = [
    path('', include(router.urls)),

    
    

]
