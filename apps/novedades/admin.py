from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'active')
    exclude = ('model_state', 'slug')
    ordering = ('-active', 'date_created')


admin.site.register(News, NewsAdmin)

# class NewsResource(resources.ModelResource):
#     class Meta:
#         model: News


# class NewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('title', 'date_created', 'active')
#     exclude = ('model_state', 'slug')
#     ordering = ('-active', 'date_created')


# admin.site.register(News, NewsAdmin)