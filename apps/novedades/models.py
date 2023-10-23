import os
from django.contrib.gis.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from apps.automatic_crud.models import BaseModel as Base


def generate_path_novedades(instance, filename):
    return os.path.join("novedades", str(instance.title).replace(' ', '-').lower(), filename)


class News(Base):
    image = models.ImageField(
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
    title = models.CharField(
        'Titulo',
        max_length=255,
    )
    subtitle = models.CharField(
        'Subtitulo',
        max_length=255,
        blank=True,
        null=True,
    )
    description = models.TextField(
        'Descripcion',
        max_length=255,
        blank=True,
        null=True,
        help_text='Texto descriptivo de la publicación (Se mostrara en la lista de publicaciones). Max. 255 caracteres.',
    )
    content = RichTextField(
        'Contenido',
        blank=True,
        null=True,
        help_text='Contenido enriquecido de la publicación'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar',
    )

    class Meta():
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id) + '-' + slugify(self.title)
            self.save()

    def __str__(self):
        return str(self.title)
