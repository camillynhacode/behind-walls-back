from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Usuario