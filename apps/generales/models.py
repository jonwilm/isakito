import requests
from django.contrib.gis.db import models
from django.db import transaction
from django.utils.html import mark_safe
from apps.automatic_crud.models import BaseModel as Base

import PIL
from PIL import Image


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
    image = models.ImageField(
        'Imagen',
        upload_to='Nosotros/',
        blank=True,
        null=True,
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
    # image = models.ImageField(
    #     'Imagen',
    #     upload_to='puntos-de-venta/',
    #     help_text='Imagen o Logo del Punto de Venta',
    #     blank=True,
    #     null=True,
    # )
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
        # help_text='Si se deja en blanco se guardara el valor segun la dirección, de lo contrario se guardara el valor ingresado manualmente',
        blank=True,
        null=True,
    )
    lng = models.CharField(
        'Longitud',
        max_length=255,
        # help_text='Si se deja en blanco se guardara el valor segun la dirección, de lo contrario se guardara el valor ingresado manualmente',
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        'Active',
        default=True,
        help_text='Activar para mostrar'
    )

    class Meta():
        verbose_name = 'Punto de Venta'
        verbose_name_plural = 'Puntos de Venta'

    def __str__(self):
        return str(self.name)


def compressImgGallery(imagen):
    image = Image.open(imagen)
    mywidth = 1000
    myheight = (1000*image.size[1])//image.size[0]
    image = image.resize((mywidth, myheight), PIL.Image.ANTIALIAS)
    return image

class GalleryHome(Base):
    image1 = models.ImageField(
        'Imagen 1',
        upload_to='gallery-home/',
        help_text='Imagen 1. Recomendado 1000x1320 o respetar relacion-aspecto para que la imagen no se corte',
    )
    link1 = models.URLField(
        'Enlace Destino Imagen 1',
        blank=True,
        null=True,
        help_text='Url de la pagina destino'
    )
    image2 = models.ImageField(
        'Imagen 2',
        upload_to='gallery-home/',
        help_text='Imagen 2. Recomendado 1000x660 o respetar relacion-aspecto para que la imagen no se corte',
    )
    link2 = models.URLField(
        'Enlace Destino Imagen 2',
        blank=True,
        null=True,
        help_text='Url de la pagina destino'
    )
    image3 = models.ImageField(
        'Imagen 3',
        upload_to='gallery-home/',
        help_text='Imagen 3. Recomendado 1000x660 o respetar relacion-aspecto para que la imagen no se corte',
    )
    link3 = models.URLField(
        'Enlace Destino Imagen 3',
        blank=True,
        null=True,
        help_text='Url de la pagina destino'
    )
    image4 = models.ImageField(
        'Imagen 4',
        upload_to='gallery-home/',
        help_text='Imagen 4. Recomendado 1000x660 o respetar relacion-aspecto para que la imagen no se corte',
    )
    link4 = models.URLField(
        'Enlace Destino Imagen 4',
        blank=True,
        null=True,
        help_text='Url de la pagina destino'
    )
    image5 = models.ImageField(
        'Imagen 5',
        upload_to='gallery-home/',
        help_text='Imagen 5. Recomendado 1000x660 o respetar relacion-aspecto para que la imagen no se corte',
    )
    link5 = models.URLField(
        'Enlace Destino Imagen 5',
        blank=True,
        null=True,
        help_text='Url de la pagina destino'
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
        # if self.image1:
        #     image = compressImgGallery(self.image1)
        #     image.save(self.image1.path)
        # if self.image2:
        #     image = compressImgGallery(self.image2)
        #     image.save(self.image2.path)
        # if self.image3:
        #     image = compressImgGallery(self.image3)
        #     image.save(self.image3.path)
        # if self.image4:
        #     image = compressImgGallery(self.image4)
        #     image.save(self.image4.path)
        # if self.image5:
        #     image = compressImgGallery(self.image5)
        #     image.save(self.image5.path)
        if not self.active:
            return super(GalleryHome, self).save(*args, **kwargs)
        with transaction.atomic():
            GalleryHome.objects.filter(active=True).update(active=False)
            return super(GalleryHome, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def show_img_1(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image1.url)
    show_img_1.short_description = 'Imagen 1'
    show_img_1.allow_tags = True
    def show_img_2(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image2.url)
    show_img_2.short_description = 'Imagen 2'
    show_img_2.allow_tags = True
    def show_img_3(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image3.url)
    show_img_3.short_description = 'Imagen 3'
    show_img_3.allow_tags = True
    def show_img_4(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image4.url)
    show_img_4.short_description = 'Imagen 4'
    show_img_4.allow_tags = True
    def show_img_5(self):
        return mark_safe(
            u'<img src="%s" height="75" />' % self.image5.url)
    show_img_5.short_description = 'Imagen 5'
    show_img_5.allow_tags = True


class Catalogo(Base):
    url = models.URLField(
        'Url Catalogo'
    )
    active = models.BooleanField(
        'Active',
        default=False,
        help_text='Activar para mostrar (Solo una URL puede estar activa)'
    )

    class Meta():
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'

    def save(self, *args, **kwargs):
        if not self.active:
            return super(Catalogo, self).save(*args, **kwargs)
        with transaction.atomic():
            Catalogo.objects.filter(active=True).update(active=False)
            return super(Catalogo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
