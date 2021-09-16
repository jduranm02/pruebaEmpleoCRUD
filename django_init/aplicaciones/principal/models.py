from django.db import models
from django.db.models.expressions import Value
class Peticion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicial=models.DateTimeField()
    fecha_final=models.DateTimeField()
    nombre_empresa=models.CharField(max_length=50)
    asunto=models.CharField(max_length=50)
    elegir_ciudad=(
                    ('Armenia','Armenia'),
                    ('Barrancabermeja','Barrancabermeja'),
                    ('Barranquilla','Barranquilla'),
                    ('Bello','Bello'),
                    ('Bogotá','Bogotá'),
                    ('Bucaramanga','Bucaramanga'),
                    ('Buenaventura','Buenaventura'),
                    ('Cali','Cali'),
                    ('Cartagena','Cartagena'),
                    ('Cúcuta','Cúcuta'),
                    ('Dosquebradas','Dosquebradas'),
                    ('Envigado','Envigado'),
                    ('Ibagué','Ibagué'),
                    ('Itagüí','Itagüí'),
                    ('Manizales','Manizales'),
                    ('Medellín','Medellín'),
                    ('Monteria','Monteria'),
                    ('Neiva','Neiva'),
                    ('Palmira','Palmira'),
                    ('Pasto','Pasto'),
                    ('Pereira','Pereira'),
                    ('Popayán','Popayán'),
                    ('Riohacha','Riohacha'),
                    ('Santa Marta','Santa Marta'),
                    ('Sincelejo','Sincelejo'),
                    ('Soacha','Soacha'),
                    ('Soledad','Soledad'),
                    ('Tuluá','Tuluá'),
                    ('Tumaco','Tumaco'),
                    ('Valledupar','Valledupar'),
                    ('Villavicencio','Villavicencio'),
                )
    ciudad=models.CharField(max_length=50,choices=elegir_ciudad)
    respuesta=models.CharField(max_length=150)
    fecha_solicitud=models.DateTimeField()
    def __str__(self):
        return self.nombre_empresa

