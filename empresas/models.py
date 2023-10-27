from pathlib import Path
from django.db import models
from usuarios.models import User, MUNICIPIOS
from vinculacion.models import Categoria
from administracion.validators import cp_validator
from django.core.validators import FileExtensionValidator
from investigadores.validators import limiteTamanioArchivo

def rutaImagenEmpresa(instance, filename):
    extension = Path(filename).suffix
    return 'usuarios/empresas/empresa_{0}{1}'.format(
        instance.encargado.pk,
        extension)

def rutaComprobanteEmpresa(instance, filename):
    extension = Path(filename).suffix
    return 'usuarios/empresas/comprobante/{0}{1}'.format(
        instance.encargado.pk,
        extension
    )


# Create your models here.
class Empresa(models.Model):
    encargado = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)
    nombre_empresa = models.CharField(max_length=80, verbose_name="Nombre")
    especialidades = models.ManyToManyField(Categoria, blank=True, verbose_name="Area del conocimiento")
    especialidad = models.CharField(max_length=255, default="")
    latitud = models.FloatField()
    longitud = models.FloatField()
    codigo_postal = models.CharField(max_length=5, validators=[cp_validator])
    municipio = models.IntegerField(choices=MUNICIPIOS)
    colonia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero_exterior = models.PositiveIntegerField()
    acerca_de = models.TextField(
        verbose_name="Acerca de",
        max_length=1000,
        default="")
    elementos = models.TextField(
        verbose_name="Elementos con los que cuenta",
        max_length=1000,
        default="")
    imagen = models.ImageField(
        upload_to=rutaImagenEmpresa,
        verbose_name="Imagen de perfil",
        blank=True,
        null=True,
        default=None)
    comprobante = models.FileField(
        upload_to=rutaComprobanteEmpresa,
        verbose_name="Oficio de comprobación",
        blank=True,
        null=True,
        default=None,
        validators=[FileExtensionValidator( ['pdf'] ), limiteTamanioArchivo]
    )

    def __str__(self):
        return self.nombre_empresa
