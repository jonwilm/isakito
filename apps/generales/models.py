import requests
from django.contrib.gis.db import models
from django.db import transaction
from django.utils.html import mark_safe
from apps.automatic_crud.models import BaseModel as Base



class Logo(Base):
    logo = models.FileField(
        'Logo',
        upload_to='logos/',
        help_text='Logo de Isakito'
    )
    active = models.BooleanField(
        'Active',
        default=False,
        help_text='Activar para mostrar (Solo un logo puede estar activo)'
    )

    class Meta():
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'

    def save(self, *args, **kwargs):
        if not self.active:
            return super(Logo, self).save(*args, **kwargs)  
        with transaction.atomic():
            Logo.objects.filter(active=True).update(active=False)
            return super(Logo, self).save(*args, **kwargs) 

    def __str__(self):
        return str(self.logo)

    def show_img(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.logo.url)
    show_img.short_description = 'Logo'
    show_img.allow_tags = True


class Contact(Base):
    address = models.CharField(
        'Direccion',
        max_length=255,
        help_text='Direccion completa'
    )
    phone = models.CharField(
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
    description = models.TextField(
        'Invitación de contacto',
        blank=True,
        null=True,
        help_text='Texto de invtacion a contactarnos'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar (Solo un registro de datos de contacto puede estar activo)'
    )

    class Meta():
        verbose_name = 'Datos de Contacto'
        verbose_name_plural = 'Datos de Contacto'

    def save(self, *args, **kwargs):
        if not self.active:
            return super(Contact, self).save(*args, **kwargs)
        with transaction.atomic():
            Contact.objects.filter(active=True).update(active=False)
            return super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.address)


SOCIAL_NETWORKS = [
    ('Instagram', 'Instagram'),
    ('Facebook', 'Facebook'),
    ('Twitter', 'X (Twitter)'),
    ('Linkedin', 'Linkedin'),
    ('TikTok', 'TikTok'),
    ('Youtube', 'Youtube'),
]

class SocialNetwork(Base):
    social_network = models.CharField(
        'Red Social',
        max_length=20,
        choices=SOCIAL_NETWORKS
    )
    url = models.URLField(
        'Url'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return str(self.social_network)


class Statistic(Base):
    title = models.CharField(
        'Título',
        max_length=50,
        help_text='Titulo de la estadística'
    )
    data = models.CharField(
        'Dato',
        max_length=50,
        help_text='Dato númerico de la estadística'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Estadística'
        verbose_name_plural = 'Estadísticas'

    def __str__(self):
        return str(self.title)


class SliderHome(Base):
    title = models.CharField(
        'Título',
        max_length=150,
        blank=True,
        null=True,
        help_text='Titulo de la imagen'
    )
    image = models.ImageField(
        'Imagen',
        upload_to='slider-home/',
        help_text='Imagen para el Slider de la Página Principal (USAR IMAGENES CON LA MISMA RELACION. RECOMENDADO, Desktop: 1920x700 Mobile: 1024x1300)'
    )
    link = models.URLField(
        'Enlace Destino',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    mobile = models.BooleanField(
        'Imagen para Mobile',
        default=False,
        help_text='Marcar para usar en la version Mobile. Desmarcar para usar en la version Desktop'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Slider Home'
        verbose_name_plural = 'Slider Home'

    def __str__(self):
        return str(self.image)

    def show_img(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image.url)
    show_img.short_description = 'Imagen'
    show_img.allow_tags = True


class Us(Base):
    title = models.CharField(
        'Título',
        max_length=150,
        blank=True,
        null=True,
        help_text='Titulo del apartado (Ej. Quienes Somos, Misión, Visión, etc...)'
    )
    text = models.TextField(
        'Texto Descriptivo',
        blank=True,
        null=True,
        help_text='Texto de descriptivo del apartado'
    )
    order = models.IntegerField(
        'Orden',
        blank=True,
        null=True,
        help_text='Orden en que aparecen los contenidos'
    )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return str(self.title)


TYPE_PLAYER = [
    ('Youtube', 'Youtube'),
    ('HTML', 'HTML'),
]

class Videos(Base):
    # type = models.CharField(
    #     'Tipo de reproductor',
    #     max_length=10,
    #     choices=TYPE_PLAYER
    # )
    title = models.CharField(
        'Titulo del video',
        max_length=255
    )
    # cover = models.ImageField(
    #     'Imagen',
    #     upload_to='slider-videos/',
    #     help_text='Imagen poster del video',
    # )
    code_yt = models.CharField(
        'Código de Youtube',
        max_length=20,
        blank=True,
        null=True,
        help_text='Código del video de youtube. **OPCIÓN RECOMENDADA** (Solo si el video esta alojado en YOUTUBE)'
    )
    # url_video = models.URLField(
    #     'Url del video',
    #     blank=True,
    #     null=True,
    #     help_text='Url del video (Solo si esta alojado en algun hosting externo)'
    # )
    # video = models.FileField(
    #     'Video',
    #     upload_to='slider-videos/',
    #     blank=True,
    #     null=True,
    #     help_text='Cargar video en servidor (Utilizar como ultima opcion)'
    # )
    active = models.BooleanField(
        'Activo',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return str(self.title)


LOCALITY = [
    ('CABA', 'CABA'),
    ('GBA', 'GBA'),
    ('INT', 'INTERIOR'),
]

class PointOfSale(Base):
    name = models.CharField(
        'Nombre',
        max_length=255
    )
    image = models.ImageField(
        'Imagen',
        upload_to='puntos-de-venta/',
        help_text='Imagen o Logo del Punto de Venta',
        blank=True,
        null=True,
    )
    address = models.CharField(
        'Direccion',
        max_length=255
    )
    locality = models.CharField(
        'Localidad',
        max_length=255,
        choices=LOCALITY
    )
    lat = models.CharField(
        'Latitud',
        max_length=255,
        help_text='Si se deja en blanco se guardara el valor segun la dirección, de lo contrario se guardara el valor ingresado manualmente',
        blank=True,
        null=True,
    )
    lng = models.CharField(
        'Longitud',
        max_length=255,
        help_text='Si se deja en blanco se guardara el valor segun la dirección, de lo contrario se guardara el valor ingresado manualmente',
        blank=True,
        null=True,
    )
    # coordinates = models.PointField(
    #     'Ubicacion en mapa',
    #     blank=True,
    #     null=True,
    # )
    active = models.BooleanField(
        'Active',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Punto de Venta'
        verbose_name_plural = 'Puntos de Venta'

    def save(self, *args, **kwargs):
        super(PointOfSale, self).save(*args, **kwargs)
        if not self.lat and not self.lng:
            url = 'https://maps.google.com/maps/api/geocode/json?address='+self.address+'&key=AIzaSyDZjvnY0GtZxL-bmhj6J32jSMxsBT8Rzm4'
            response = requests.get(url)
            print(response.json())
    #         self.lat = response.json()['results'][0]['geometry']['location']['lat']
    #         self.lng = response.json()['results'][0]['geometry']['location']['lng']
    #         self.save()

    def __str__(self):
        return str(self.name)


class GalleryHome(Base):
    imageV1 = models.ImageField(
        'Imagen Vertical 1',
        upload_to='gallery-home/',
        help_text='Imagen en Formato Vertical. Recomendado 800x1400',
    )
    linkV1 = models.URLField(
        'Enlace Destino Imagen Vertical 1',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    imageV2 = models.ImageField(
        'Imagen Vertical 2',
        upload_to='gallery-home/',
        help_text='Imagen en Formato Vertical. Recomendado 800x1400',
    )
    linkV2 = models.URLField(
        'Enlace Destino Imagen Vertical 2',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    imageH1 = models.ImageField(
        'Imagen Horizontal 1',
        upload_to='gallery-home/',
        help_text='Imagen en Formato Horizontal. Recomendado 1400x550',
    )
    linkH1 = models.URLField(
        'Enlace Destino Imagen Horizontal 1',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    imageH2 = models.ImageField(
        'Imagen Horizontal 2',
        upload_to='gallery-home/',
        help_text='Imagen en Formato Horizontal. Recomendado 1400x550',
    )
    linkH2 = models.URLField(
        'Enlace Destino Imagen Horizontal 2',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    imageC = models.ImageField(
        'Imagen Central',
        upload_to='gallery-home/',
        help_text='Imagen Central. Recomendado 800x550',
    )
    linkC = models.URLField(
        'Enlace Destino Imagen Central',
        blank=True,
        null=True,
        help_text='Url de la pagina destino al hacer click'
    )
    active = models.BooleanField(
        'Active',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Galeria Home'
        verbose_name_plural = 'Galeria Home'

    def save(self, *args, **kwargs):
        if not self.active:
            return super(GalleryHome, self).save(*args, **kwargs)
        with transaction.atomic():
            GalleryHome.objects.filter(active=True).update(active=False)
            return super(GalleryHome, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def show_img_V1(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imageV1.url)
    show_img_V1.short_description = 'Imagen Vertical 1'
    show_img_V1.allow_tags = True
    def show_img_V2(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imageV2.url)
    show_img_V2.short_description = 'Imagen Vertical 2'
    show_img_V2.allow_tags = True
    def show_img_H1(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imageH1.url)
    show_img_H1.short_description = 'Imagen Horizontal 1'
    show_img_H1.allow_tags = True
    def show_img_H2(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imageH2.url)
    show_img_H2.short_description = 'Imagen Horizontal 2'
    show_img_H2.allow_tags = True
    def show_img_C(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.imageC.url)
    show_img_C.short_description = 'Imagen Central'
    show_img_C.allow_tags = True
