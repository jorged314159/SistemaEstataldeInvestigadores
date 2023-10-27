# Generated by Django 4.1.3 on 2023-10-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinculacion', '0007_alter_noticia_fecha'),
        ('empresas', '0012_empresa_comprobante'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='elementos',
            field=models.TextField(default='', max_length=1000, verbose_name='Elementos con los que cuenta'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='especialidad',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='especialidades',
            field=models.ManyToManyField(blank=True, to='vinculacion.categoria', verbose_name='Area del conocimiento'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre_empresa',
            field=models.CharField(max_length=80, verbose_name='Nombre'),
        ),
    ]
