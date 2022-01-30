from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins

from usuarios.models import Usuario

from .serializers import UsuarioSerializer

class UsuarioviewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer


