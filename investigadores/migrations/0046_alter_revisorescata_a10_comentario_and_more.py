# Generated by Django 4.1.3 on 2023-09-16 20:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0045_alter_revisorescata_a10_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisorescata',
            name='a10_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A10 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a1_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A1 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a2_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A2 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a3_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A3 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a4_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A4 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a5_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A5 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a6_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A6 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a7_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A7 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a8_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A8 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a9_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A9 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b10_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B10 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b1_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B1 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b2_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B2 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b3_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B3 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b4_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B4 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b5_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B5 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b6_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B6 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b7_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B7 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b8_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B8 (Minimo 250 caracteres)'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b9_comentario',
            field=models.TextField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(250)], verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B9 (Minimo 250 caracteres)'),
        ),
    ]