from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm, CustomUsuarioChanceForms
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form =  CustomUsuarioChanceForms
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'fone','is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissõe', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dadas Importantes', {'fields': ('last_login', 'date_joined')}),)
