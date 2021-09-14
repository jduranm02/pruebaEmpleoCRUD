from django.db import models

class Peticion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicial=models.DateTimeField()
    fecha_final=models.DateTimeField()
    nombre_empresa=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    asunto=models.CharField(max_length=50)
    respuesta=models.CharField(max_length=150)
    fecha_solicitud=models.DateTimeField()

    def __str__(self):
        return self.nombre_empresa

