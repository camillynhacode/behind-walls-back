from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
import re

from .manager import UserManager

# Create your models here.
class Usuario(AbstractBaseUser,PermissionsMixin):
    nome= models.CharField(
        verbose_name= "Nome Completo",
        max_length= 80
    )
    username = models.CharField(
        verbose_name='username',
        max_length=15,
        unique=True,
        validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            ('Enter a valid username.'),
            ('invalid'))
        ]
    )
    rg= models.CharField(
        verbose_name= "RG",
        max_length= 11
    )
    contato= models.CharField(
        verbose_name= "Telefone ou Celular",
        max_length= 15
    )
    email= models.CharField(
        verbose_name= "E-mail",
        max_length= 60,
        unique= True

    )
    cep= models.CharField(
        verbose_name= "CEP",
        max_length= 15
    )
    zona= models.CharField(
        verbose_name= "Zona",
        max_length= 60
    )
    bairro= models.CharField(
        verbose_name= "Bairro",
        max_length= 60
    )
    rua= models.CharField(
        verbose_name= "Rua",
        max_length= 60
    )
    
    first_name = models.CharField(verbose_name=('first name'), max_length=30)
    last_name = models.CharField(verbose_name=('last name'), max_length=30)

    is_staff = models.BooleanField(
        verbose_name=('staff status'),
        default=False,
    )
    is_active = models.BooleanField(verbose_name=('active'),
        default=True,
    )

    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)
    
    objects = UserManager()
    
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS = ['username']


    class Meta:
        app_label="usuarios"
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def get_full_name(self):
        return self.nome