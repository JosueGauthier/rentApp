from rest_framework import viewsets
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username',
                        'is_staff', 'groups', 'is_active']
