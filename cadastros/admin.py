from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# importar as classes

from .models import Paciente, UnidadeSolicitante, UnidadeExecutante, Procedimento, VagaOfertada, UserUnidade

class UserUnidadeInline(admin.StackedInline):
    model = UserUnidade
    verbose_name = "Selecione uma unidade para"
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserUnidadeInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Paciente)
admin.site.register(UnidadeSolicitante)
admin.site.register(UnidadeExecutante)
admin.site.register(Procedimento)
admin.site.register(VagaOfertada)
