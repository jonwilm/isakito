from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from .models import Logo, Contacto, RedSocial, Estadistica, SliderHome, Nosotros, Videos, PuntoDeVenta


class LogoResource(resources.ModelResource):
    class Meta:
        model: Logo


class LogoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('show_img', 'logo', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


class ContactoResource(resources.ModelResource):
    class Meta:
        model: Contacto


class ContactoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('direccion', 'telefono', 'email', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


class RedSocialResource(resources.ModelResource):
    class Meta:
        model: RedSocial


class RedSocialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('red_social', 'url', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


class EstadisticaResource(resources.ModelResource):
    class Meta:
        model: Estadistica


class EstadisticaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('titulo', 'dato', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


class SliderHomeResource(resources.ModelResource):
    class Meta:
        model: SliderHome


class SliderHomeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('show_img', 'titulo', 'enlace', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


class NosotrosResource(resources.ModelResource):
    class Meta:
        model: Nosotros


class NosotrosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('titulo', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


class VideosResource(resources.ModelResource):
    class Meta:
        model: Videos


class VideosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


# class PuntoDeVentaResource(resources.ModelResource):
#     class Meta:
#         model: PuntoDeVenta


class PuntoDeVentaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
    list_display = ('nombre', 'activo')
    exclude = ('model_state',)
    ordering = ('-activo',)


admin.site.register(Logo, LogoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(RedSocial, RedSocialAdmin)
admin.site.register(Estadistica, EstadisticaAdmin)
admin.site.register(SliderHome, SliderHomeAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(PuntoDeVenta, PuntoDeVentaAdmin)
