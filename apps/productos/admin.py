from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models

from .models import Marca, SliderMarca, Producto


class SliderMarcaResource(resources.ModelResource):
    class Meta:
        model: SliderMarca


class SliderMarcaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('marca', 'show_img', 'titulo', 'orden', 'activo')
    exclude = ('model_state',)
    list_filter = ('marca',)
    ordering = ('-activo',)


class SliderMarcaInlineAdmin(admin.TabularInline):
    model = SliderMarca
    exclude = ('model_state',)
    extra = 0


class MarcaResource(resources.ModelResource):
    class Meta:
        model: Marca


class MarcaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = (SliderMarcaInlineAdmin,)
    list_display = ('show_img', 'nombre', 'activo')
    exclude = ('model_state',)
    list_filter = ('nombre',)
    ordering = ('-activo',)


class ProductoResource(resources.ModelResource):
    class Meta:
        model: Producto


class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('sku', 'titulo', 'marca', 'activo')
    exclude = ('model_state',)
    list_filter = ('marca',)
    ordering = ('-activo',)


admin.site.register(Marca, MarcaAdmin)
admin.site.register(SliderMarca, SliderMarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
