# Generated by Django 5.0.4 on 2024-05-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0021_alter_personajes_nombre_alter_personajes_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajes',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personajes',
            name='serie',
            field=models.CharField(max_length=100),
        ),
    ]
