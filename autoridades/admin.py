from django.contrib import admin
from .models import Autoridade
# Register your models here.
@admin.register(Autoridade)
class AutoridadeAdmin(admin.ModelAdmin):
    pass 