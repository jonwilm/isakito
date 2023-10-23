from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models

from .models import Brand, SliderBrand, Product, ImagesProduct, ImportProducts


class SliderBrandResource(resources.ModelResource):
    class Meta:
        model: SliderBrand


class SliderBrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('brand', 'show_img', 'title', 'order', 'active')
    exclude = ('model_state',)
    list_filter = ('brand',)
    ordering = ('-active',)


class SliderBrandInlineAdmin(admin.TabularInline):
    model = SliderBrand
    exclude = ('model_state',)
    extra = 0


class BrandResource(resources.ModelResource):
    class Meta:
        model: Brand


class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = (SliderBrandInlineAdmin,)
    list_display = ('name', 'show_img', 'active')
    exclude = ('model_state', 'slug')
    list_filter = ('name',)
    ordering = ('-active',)


class ImagenesProductInlineAdmin(admin.TabularInline):
    model = ImagesProduct
    exclude = ('model_state',)
    extra = 0


class ProductResource(resources.ModelResource):
    class Meta:
        model: Product


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = (ImagenesProductInlineAdmin,)
    list_display = ('sku', 'title', 'brand', 'active')
    exclude = ('model_state', 'slug')
    list_filter = ('brand',)
    ordering = ('-active',)


class ImagenesProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product', 'image', 'active')
    exclude = ('model_state',)
    list_filter = ('product',)
    ordering = ('-active',)


class ImportarProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'status')
    exclude = ('model_state',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(SliderBrand, SliderBrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ImagesProduct, ImagenesProductAdmin)
admin.site.register(ImportProducts, ImportarProductsAdmin)
