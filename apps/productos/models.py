import os
from django.db import models, transaction
from django.utils.html import mark_safe
from django.utils.text import slugify
from apps.automatic_crud.models import BaseModel as Base

from apps.generales.models import PuntoDeVenta


class Marca(Base):
    nombre = models.CharField(
        'Nombre',
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(
        'URL',
        max_length=255,
        unique=True,
    )
    logo = models.FileField(
        'Logo',
        upload_to='marcas/',
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

    def save(self, *args, **kwargs):
        super(Marca, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.nombre)
            self.save()

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
        verbose_name='Marca',
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
        unique=True,
    )
    titulo = models.CharField(
        'Titulo',
        max_length=255,
    )
    slug = models.SlugField(
        'URL',
        max_length=255,
        unique=True,
    )
    descripcion = models.TextField(
        'Descripción',
        blank=True,
        null=True,
    )
    precio = models.CharField(
        'Precio',
        # max_digits=10,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    ean = models.CharField(
        'EAN',
        max_length=20,
        blank=True,
        null=True,
    )
    categoria = models.CharField(
        'Categoria',
        max_length=150,
        blank=True,
        null=True,
    )
    marca = models.ForeignKey(
        Marca,
        verbose_name='Marca',
        on_delete=models.CASCADE,
    )
    stock = models.CharField(
        'Stock',
        max_length=20,
        blank=True,
        null=True,
    )
    # stock = models.IntegerField(
    #     'Stock',
    #     default=0
    # )
    proveedor = models.CharField(
        'Proveedor',
        max_length=150,
        blank=True,
        null=True,
    )
    alto = models.CharField(
        'Alto',
        # max_digits=5,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    ancho = models.CharField(
        'Ancho',
        # max_digits=5,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    largo = models.CharField(
        'Largo',
        # max_digits=5,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    peso = models.CharField(
        'Peso',
        # max_digits=10,
        # decimal_places=2,
        max_length=20,
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
    puntos_venta = models.ManyToManyField(
        PuntoDeVenta,
        verbose_name='Puntos de Venta',
        blank=True,
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )
    
    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def save(self, *args, **kwargs):
        super(Producto, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.sku) + '-' + slugify(self.titulo)
            self.save()

    def __str__(self):
        return str(self.sku)


class ImagenesProducto(Base):
    producto = models.ForeignKey(
        Producto,
        verbose_name='Producto',
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


STATUS_EXCEL = (
    ('1', 'Por Importar'),
    ('2', 'Importado'),
    ('3', 'Error al Importar'),
)

class ImportarProductos(Base):
    documento = models.FileField(
        'Excel de productos',
        upload_to='excels-productos/',
    )
    status = models.CharField(
        'Estado',
        max_length=1,
        choices=STATUS_EXCEL,
        default='1',
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Importar Producto'
        verbose_name_plural = 'Importar Productos'
