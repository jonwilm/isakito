from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models

from .models import Novedad


class NovedadResource(resources.ModelResource):
    class Meta:
        model: Novedad


class NovedadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'activo')
    exclude = ('model_state', 'slug')
    ordering = ('-activo', 'fecha_creacion')


admin.site.register(Novedad, NovedadAdmin)