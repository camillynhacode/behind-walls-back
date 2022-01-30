from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from usuarios.models import Usuario

from .serializers import UsuarioSerializer

class UsuarioviewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

    def retrive(self, request):
        queryset = self.queryset.filter(usuario=request.user)
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)