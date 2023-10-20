from django.db import models, transaction
from django.utils.html import mark_safe
from apps.automatic_crud.models import BaseModel as Base


class Logo(Base):
    logo = models.FileField(
        'Logo',
        upload_to='media/logos/',
        help_text='Logo de Isakito'
    )
    activo = models.BooleanField(
        'Activo',
        default=False,
        help_text='Activar para mostrar (Solo un logo puede estar activo)'
    )

    class Meta():
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'

    def save(self, *args, **kwargs):
        if not self.activo:
            return super(Logo, self).save(*args, **kwargs)  
        with transaction.atomic():
            Logo.objects.filter(activo=True).update(activo=False)
            return super(Logo, self).save(*args, **kwargs) 

    def __str__(self):
        return str(self.logo)

    def show_img(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.logo.url)
    show_img.short_description = 'Logo'
    show_img.allow_tags = True


class Contacto(Base):
    direccion = models.CharField(
        'Direccion',
        max_length=255,
        help_text='Direccion completa'
    )
    telefono = models.CharField(
        'Teléfono',
        max_length=20,
    )
    whatsapp = models.CharField(
        'Whatsapp',
        max_length=20,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        'Correo eléctronico',
        help_text='Correo eléctronico de contacto'
    )
    email_form = models.EmailField(
        'Correo eléctronico formulario',
        help_text='Correo eléctronico destino del formulario de contacto'
    )
    descripcion = models.TextField(
        'Invitación de contacto',
        blank=True,
        null=True,
        help_text='Texto de invtacion a contactarnos'
    )
    activo = models.BooleanField(
        'Activo',
        default=False,
        help_text='Activar para mostrar (Solo un registro de datos de contacto puede estar activo)'
    )

    class Meta():
        verbose_name = 'Dato de Contacto'
        verbose_name_plural = 'Datos de Contacto'

    def save(self, *args, **kwargs):
        if not self.activo:
            return super(Contacto, self).save(*args, **kwargs)
        with transaction.atomic():
            Contacto.objects.filter(activo=True).update(activo=False)
            return super(Contacto, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.direccion)


REDES_SOCIALES = [
    ('ig', 'Instagram'),
    ('fb', 'facebook'),
    ('x', 'X (Twitter'),
    ('in', 'Linkedin'),
    ('tk', 'TikTok'),
    ('yt', 'Youtube'),
]

class RedSocial(Base):
    red_social = models.CharField(
        'Red Social',
        max_length=2,
        choices=REDES_SOCIALES
    )
    url = models.URLField(
        'Url'
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return str(self.red_social)


class Estadistica(Base):
    titulo = models.CharField(
        'Título',
        max_length=50,
        help_text='Titulo de la estadística'
    )
    dato = models.CharField(
        'Título',
        max_length=50,
        help_text='Dato númerico de la estadística'
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Estadística'
        verbose_name_plural = 'Estadísticas'

    def __str__(self):
        return str(self.titulo)


class SliderHome(Base):
    titulo = models.CharField(
        'Título',
        max_length=150,
        blank=True,
        null=True,
        help_text='Titulo de la imagen'
    )
    imagen = models.ImageField(
        'Imagen',
        upload_to='media/slider-home/',
        help_text='Imagen para el Slider de la Página Principal'
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
        verbose_name = 'Slider Home'
        verbose_name_plural = 'Slider Home'

    def __str__(self):
        return str(self.imagen)

    def show_img(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imagen.url)
    show_img.short_description = 'Imagen'
    show_img.allow_tags = True


class Nosotros(Base):
    titulo = models.CharField(
        'Título',
        max_length=150,
        blank=True,
        null=True,
        help_text='Titulo del apartado (Ej. Quienes Somos, Misión, Visión, etc...'
    )
    texto = models.TextField(
        'Texto Descriptivo',
        blank=True,
        null=True,
        help_text='Texto de descriptivo del apartado'
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return str(self.titulo)


TIPO_REPRODUCTOR = [
    ('yt', 'Youtube'),
    ('html', 'HTML'),
]

class Videos(Base):
    tipo = models.CharField(
        'Tipo de reproductor',
        max_length=4,
        choices=TIPO_REPRODUCTOR
    )
    titulo = models.CharField(
        'Titulo del video',
        max_length=255
    )
    codigo_yt = models.CharField(
        'Código de Youtube',
        max_length=20,
        blank=True,
        null=True,
        help_text='Código del video de youtube. **OPCIÓN RECOMENDADA** (Solo si el video esta alojado en YOUTUBE)'
    )
    url_video = models.URLField(
        'Url del video',
        blank=True,
        null=True,
        help_text='Url del video (Solo si esta alojado en algun hosting externo)'
    )
    video = models.FileField(
        'Video',
        upload_to='media/slider-videos/',
        blank=True,
        null=True,
        help_text='Cargar video en servidor (Utilizar como ultima opcion)'
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return str(self.titulo)


class PuntoDeVenta(Base):
    nombre = models.CharField(
        'Nombre',
        max_length=255
    )
    imagen = models.ImageField(
        'Imagen',
        upload_to='media/puntos-de-venta/',
        help_text='Imagen o Logo del Punto de Venta',
        blank=True,
        null=True,
    )
    direccion = models.CharField(
        'Direccion',
        max_length=255
    )
    localidad = models.CharField(
        'Localidad',
        max_length=255
    )
    latitud = models.CharField(
        'latitud',
        max_length=255
    )
    longitud = models.CharField(
        'longitud',
        max_length=255
    )
    activo = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Punto de Venta'
        verbose_name_plural = 'Puntos de Venta'

    def __str__(self):
        return str(self.nombre)
