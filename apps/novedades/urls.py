from django.urls import path

from . import views

app_name = "novedades_app"

urlpatterns = [
    path(
        '',
        views.NewsListView.as_view(),
        name='novedades',
    ),
    path(
        'nosotros',
        views.NewsView.as_view(),
        name='novedad',
    ),
]
