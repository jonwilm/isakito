from django.urls import path

from . import views

app_name = "generales_app"

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home',
    ),
    path(
        'nosotros',
        views.UsView.as_view(),
        name='us',
    ),
    path(
        'contacto',
        views.ContactView.as_view(),
        name='contacto',
    ),
    path(
        'puntos-de-venta',
        views.PointOfSaleView.as_view(),
        name='puntos-de-venta',
    ),
    path(
        'sendmail',
        views.MailContact,
        name='contact-mail',
    ),
]
