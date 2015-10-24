from django.db import models


class Cancha(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __unicode__(self):
        return self.nombre


class Telefono(models.Model):
    numero = models.CharField(max_length=15)
    cancha = models.ForeignKey(Cancha, related_name="telefonos", related_query_name="telefono")

    def __unicode__(self):
        return self.numero