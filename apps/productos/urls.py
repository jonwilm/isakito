from django.urls import path

from . import views

app_name = "productos_app"

urlpatterns = [
    path(
        'marcas',
        views.BrandsView.as_view(),
        name='marcas',
    ),
    path(
        'marcas/<slug:slug>',
        views.BrandView.as_view(),
        name="marca",
    ),
]
