from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from usuarios.models import Usuario

from .serializers import UsuarioSerializer

class UsuarioviewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer
