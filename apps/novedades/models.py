import os
from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from apps.automatic_crud.models import BaseModel as Base


def generate_path_novedades(instance, filename):
    return os.path.join("media/novedades", str(instance.titulo).replace(' ', '-').lower(), filename)


class Novedad(Base):
    imagen = models.ImageField(
        'Imagen Destacada',
        upload_to=generate_path_novedades,
        blank=True,
        null=True,
        help_text='Imagen destacada del Post'
    )
    slug = models.SlugField(
        'URL',
        max_length=255,
        unique=True,
    )
    titulo = models.CharField(
        'Titulo',
        max_length=255,
    )
    subtitulo = models.CharField(
        'Subtitulo',
        max_length=255,
        blank=True,
        null=True,
    )
    fecha_creacion = models.DateField(
        'Fecha de creación',
        auto_now=False,
        auto_now_add=True,
    )
    descripcion = models.TextField(
        'Descripcion',
        max_length=255,
        blank=True,
        null=True,
        help_text='Texto descriptivo de la publicación (Se mostrara en la lista de publicaciones). Max. 255 caracteres.',
    )
    contenido = RichTextField(
        'Contenido',
        blank=True,
        null=True,
        help_text='Contenido enriquecido de la publicación'
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar',
    )

    class Meta():
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'

    def save(self, *args, **kwargs):
        super(Novedad, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id) + '-' + slugify(self.titulo)
            self.save()

    def __str__(self):
        return str(self.titulo)
