from django.db import models


# Create your models here.

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=24)
    numero_camiseta = models.PositiveIntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return f"{self.nombre} - #{self.numero_camiseta} ({self.equipo_futbol.nombre})"


class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    nombre_auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_campeonato


class CampeonatoEquipos(models.Model):
    anio = models.PositiveIntegerField()
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE, related_name="campeonatos")
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name="equipos")

    class Meta:
        unique_together = ('año', 'equipo_futbol', 'campeonato')

    def __str__(self):
        return f"{self.año} - {self.equipo_futbol.nombre} in {self.campeonato.nombre_campeonato}"
