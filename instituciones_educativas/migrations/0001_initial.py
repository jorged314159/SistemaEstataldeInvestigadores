# Generated by Django 4.0.4 on 2022-06-17 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0007_remove_institucioneducativa_ubicacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitucionEducativa',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre_institucion', models.CharField(max_length=80)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
    ]
