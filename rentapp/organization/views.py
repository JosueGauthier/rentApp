from rest_framework import viewsets
from django.contrib.auth.models import User
""" from django_filters.rest_framework import DjangoFilterBackend
 """

from .models import *

from .serializers import *

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    """ filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop', 'name'] """


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
