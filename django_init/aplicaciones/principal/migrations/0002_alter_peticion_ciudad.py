# Generated by Django 3.2.7 on 2021-09-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peticion',
            name='ciudad',
            field=models.CharField(blank=True, choices=[('Armenia', 'Armenia'), ('Barrancabermeja', 'Barrancabermeja'), ('Barranquilla', 'Barranquilla'), ('Bello', 'Bello'), ('Bogotá', 'Bogotá'), ('Bucaramanga', 'Bucaramanga'), ('Buenaventura', 'Buenaventura'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Cúcuta', 'Cúcuta'), ('Dosquebradas', 'Dosquebradas'), ('Envigado', 'Envigado'), ('Ibagué', 'Ibagué'), ('Itagüí', 'Itagüí'), ('Manizales', 'Manizales'), ('Medellín', 'Medellín'), ('Monteria', 'Monteria'), ('Neiva', 'Neiva'), ('Palmira', 'Palmira'), ('Pasto', 'Pasto'), ('Pereira', 'Pereira'), ('Popayán', 'Popayán'), ('Riohacha', 'Riohacha'), ('Santa Marta', 'Santa Marta'), ('Sincelejo', 'Sincelejo'), ('Soacha', 'Soacha'), ('Soledad', 'Soledad'), ('Tuluá', 'Tuluá'), ('Tumaco', 'Tumaco'), ('Valledupar', 'Valledupar'), ('Villavicencio', 'Villavicencio')], max_length=50),
        ),
    ]
