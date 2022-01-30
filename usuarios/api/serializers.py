from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        fields=[
            'bairro',
            'cep',
            'contato',
            'email',
            'first_name',
            'last_name',
            'nome',
            'password',
            'rg',
            'rua',
            'username',
            'zona',
        ]
        model=Usuario