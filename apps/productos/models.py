import os
from django.db import models, transaction
from django.utils.html import mark_safe
from django.utils.text import slugify
from apps.automatic_crud.models import BaseModel as Base

from apps.generales.models import PointOfSale


class Brand(Base):
    name = models.CharField(
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
        upload_to='brands/',
        blank=True,
        null=True,
        help_text='Logo de la Marca'
    )
    description = models.TextField(
        'Descripcion',
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar',
    )

    class Meta():
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def save(self, *args, **kwargs):
        super(Brand, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name)
            self.save()

    def __str__(self):
        return str(self.name)

    def show_img(self):
        if self.logo:
            return mark_safe(
                u'<img src="%s" height="75" />' % self.logo.url)
    show_img.short_description = 'Logo'
    show_img.allow_tags = True


def generate_path_marca(instance, filename):
    return os.path.join("marcas", str(instance.brand.name).replace(' ', '-').lower(), "slider", filename)


class SliderBrand(Base):
    brand = models.ForeignKey(
        Brand,
        verbose_name='Marca',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        'Título',
        max_length=150,
        blank=True,
        null=True,
        help_text='Titulo de la imagen'
    )
    image = models.ImageField(
        'Imagen',
        upload_to=generate_path_marca,
        help_text='Imagen para el Slider de la Marca (USAR IMAGENES CON LA MISMA RELACION. RECOMENDADO 1920x700)'
    )
    order = models.IntegerField(
        'Orden',
        blank=True,
        null=True,
        help_text='Orden en que aparecen las imagenes en el slider'
    )
    link = models.URLField(
        'Enlace Destino',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Slider Marca'
        verbose_name_plural = 'Slider Marca'

    def __str__(self):
        return str(self.image)

    def show_img(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image.url)
    show_img.short_description = 'Imagen'
    show_img.allow_tags = True


class Product(Base):
    sku = models.CharField(
        'SKU',
        max_length=20,
        unique=True,
    )
    title = models.CharField(
        'Titulo',
        max_length=255,
    )
    slug = models.SlugField(
        'URL',
        max_length=255,
        unique=True,
    )
    image = models.URLField(
        'Url de la Imagen',
        blank=True,
        null=True,
    )
    description = models.TextField(
        'Descripción',
        blank=True,
        null=True,
    )
    price = models.CharField(
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
    category = models.CharField(
        'Categoria',
        max_length=150,
        blank=True,
        null=True,
    )
    brand = models.ForeignKey(
        Brand,
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
    supplier = models.CharField(
        'Proveedor',
        max_length=150,
        blank=True,
        null=True,
    )
    height = models.CharField(
        'Alto',
        # max_digits=5,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    width = models.CharField(
        'Ancho',
        # max_digits=5,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    long = models.CharField(
        'Largo',
        # max_digits=5,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    weight = models.CharField(
        'Peso',
        # max_digits=10,
        # decimal_places=2,
        max_length=20,
        blank=True,
        null=True,
    )
    video = models.CharField(
        'Código de Youtube',
        max_length=20,
        blank=True,
        null=True,
        help_text='Código del video de youtube. **OPCIÓN RECOMENDADA** (Solo si el video esta alojado en YOUTUBE)'
    )
    age = models.CharField(
        'Edad',
        max_length=20,
        blank=True,
        null=True,
    )
    points_of_sale = models.ManyToManyField(
        PointOfSale,
        verbose_name='Puntos de Venta',
        blank=True,
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )
    
    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.sku) + '-' + slugify(self.title)
            self.save()

    def __str__(self):
        return str(self.sku)


class ImagesProduct(Base):
    product = models.ForeignKey(
        Product,
        verbose_name='Producto',
        on_delete=models.CASCADE,
    )
    image = models.URLField(
        'Url de la Imagen',
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Imagen de Producto'
        verbose_name_plural = 'Imagenes de Producto'

    def __str__(self):
        return str(self.image)


STATUS_EXCEL = (
    ('1', 'Por Importar'),
    ('2', 'Importado'),
    ('3', 'Error al Importar'),
)

class ImportProducts(Base):
    document = models.FileField(
        'Excel de productos',
        upload_to='excels-products/',
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
