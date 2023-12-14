from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from .models import Logo, Contact, SocialNetwork, Statistic, SliderHome, Us, Videos, PointOfSale, GalleryHome, Catalogo


class LogoResource(resources.ModelResource):
    class Meta:
        model: Logo


class LogoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('show_img', 'logo', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class ContactResource(resources.ModelResource):
    class Meta:
        model: Contact


class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class SocialNetworkResource(resources.ModelResource):
    class Meta:
        model: SocialNetwork


class SocialNetworkAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('social_network', 'url', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class StatisticResource(resources.ModelResource):
    class Meta:
        model: Statistic


class StatisticAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'data', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class SliderHomeResource(resources.ModelResource):
    class Meta:
        model: SliderHome


class SliderHomeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('show_img', 'title', 'link', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class UsResource(resources.ModelResource):
    class Meta:
        model: Us


class UsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'order', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class VideosResource(resources.ModelResource):
    class Meta:
        model: Videos


class VideosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class PointOfSaleResource(resources.ModelResource):
    class Meta:
        model: PointOfSale


class PointOfSaleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'address', 'active')
    list_filter = ('locality',)
    exclude = ('model_state',)
    ordering = ('-active', 'name',)


class GalleryHomeResource(resources.ModelResource):
    class Meta:
        model: GalleryHome


class GalleryHomeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'show_img_1', 'show_img_2', 'show_img_3', 'show_img_4', 'show_img_5', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


class CatalogoResource(resources.ModelResource):
    class Meta:
        model: Catalogo


class CatalogoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('url', 'active')
    exclude = ('model_state',)
    ordering = ('-active',)


admin.site.register(Logo, LogoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(SliderHome, SliderHomeAdmin)
admin.site.register(Us, UsAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(PointOfSale, PointOfSaleAdmin)
admin.site.register(GalleryHome, GalleryHomeAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
