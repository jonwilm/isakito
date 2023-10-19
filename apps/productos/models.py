import os
from django.db import models, transaction
from django.utils.html import mark_safe
from apps.automatic_crud.models import BaseModel as Base


class Marca(Base):
    nombre = models.CharField(
        'Nombre',
        max_length=100,
    )
    logo = models.FileField(
        'Logo',
        upload_to='media/marcas/',
        blank=True,
        null=True,
        help_text='Logo de la Marca'
    )
    descripcion = models.TextField(
        'Descripcion',
        blank=True,
        null=True,
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar',
    )

    class Meta():
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return str(self.nombre)

    def show_img(self):
        if self.logo:
            return mark_safe(
                u'<img src="%s" height="75" />' % self.logo.url)
    show_img.short_description = 'Logo'
    show_img.allow_tags = True


def generate_path_marca(instance, filename):
    return os.path.join("media/marcas", str(instance.marca.nombre).replace(' ', '-').lower(), "slider", filename)


class SliderMarca(Base):
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
    )
    titulo = models.CharField(
        'Título',
        max_length=150,
        blank=True,
        null=True,
        help_text='Titulo de la imagen'
    )
    imagen = models.ImageField(
        'Imagen',
        upload_to=generate_path_marca,
        help_text='Imagen para el Slider de la Marca'
    )
    orden = models.IntegerField(
        'Orden',
        blank=True,
        null=True,
        help_text='Orden en que aparecen las imagenes en el slider'
    )
    enlace = models.URLField(
        'Enlace Destino',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Slider Marca'
        verbose_name_plural = 'Slider Marca'

    def __str__(self):
        return str(self.imagen)

    def show_img(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imagen.url)
    show_img.short_description = 'Imagen'
    show_img.allow_tags = True


class Producto(Base):
    sku = models.CharField(
        'SKU',
        max_length=20,
    )
    titulo = models.CharField(
        'Titulo',
        max_length=255,
    )
    descripcion = models.TextField(
        'Descripción',
    )
    precio = models.DecimalField(
        'Precio',
        max_digits=10,
        decimal_places=2
    )
    ean = models.CharField(
        'EAN',
        max_length=20,
    )
    categoria = models.CharField(
        'Categoria',
        max_length=100,
    )
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.CASCADE,
    )
    stock = models.IntegerField(
        'Stock',
        default=0
    )
    proveedor = models.CharField(
        'Proveedor',
        max_length=255,
    )
    alto = models.CharField(
        'Alto',
        max_length=255,
        blank=True,
        null=True,
    )
    ancho = models.CharField(
        'Ancho',
        max_length=255,
        blank=True,
        null=True,
    )
    largo = models.CharField(
        'Largo',
        max_length=255,
        blank=True,
        null=True,
    )
    peso = models.CharField(
        'Peso',
        max_length=255,
        blank=True,
        null=True,
    )
    video = models.URLField(
        'Url del video',
        blank=True,
        null=True,
    )
    edad = models.CharField(
        'Edad',
        max_length=20,
        blank=True,
        null=True,
    )
    puntos_venta = models.CharField(
        'Donde comprar',
        max_length=255,
        blank=True,
        null=True,
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )
    
    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.imagen)


class ImagenesProducto(Base):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
    )
    imagen = models.URLField(
        'Url de la Imagen',
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Imagen de Producto'
        verbose_name_plural = 'Imagenes de Producto'

    def __str__(self):
        return str(self.imagen)