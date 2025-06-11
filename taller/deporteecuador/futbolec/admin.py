from django.contrib import admin
from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos

class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'username_twitter')
    search_fields = ('nombre', 'siglas')

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo_futbol')
    list_filter = ('posicion_campo', 'equipo_futbol')
    search_fields = ('nombre',)

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato',)

class CampeonatoEquiposAdmin(admin.ModelAdmin):
    list_display = ('anio', 'equipo_futbol', 'campeonato')
    list_filter = ('anio', 'campeonato')

admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
admin.site.register(EquipoFutbol, EquipoFutbolAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
