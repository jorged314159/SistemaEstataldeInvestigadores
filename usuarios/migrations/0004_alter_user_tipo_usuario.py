# Generated by Django 4.0.4 on 2022-06-07 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_tipousuario_alter_user_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.tipousuario'),
        ),
    ]
