from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework import viewsets, views
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions

from reservation.views import check_reservation_for_non_consumable



from .models import *

from .serializers import *


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'organization']


class ProductViewSet(viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        check_reservation_for_non_consumable()
        return response
            
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'category',
                        'is_active', 'is_removed', 'qty_total', 'qty_available', 'is_consumable']
