# Generated by Django 5.0.4 on 2024-04-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_imagen_alter_recetas_categoria_alter_recetas_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='categoria',
            field=models.CharField(choices=[('Recetas', 'Recetas'), ('Recetas Saladas', 'Recetas Saladas'), ('Recetas Dulces', 'Recetas Dulces')], default='Recetas', max_length=100),
        ),
    ]
