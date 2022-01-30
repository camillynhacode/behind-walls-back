from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

from usuarios.models import Usuario

from .serializers import UsuarioSerializer

class UsuarioviewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        user = Usuario.objects.get(username=serializer['username'].value)
        user.set_password(serializer['password'].value)
        user.save()

