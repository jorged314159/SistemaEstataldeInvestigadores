# Generated by Django 4.0.4 on 2022-06-20 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='user',
            new_name='encargado',
        ),
    ]
