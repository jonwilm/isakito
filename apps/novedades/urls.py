from django.urls import path

from . import views

app_name = "novedades_app"

urlpatterns = [
    path(
        'novedades',
        views.NewsListView.as_view(),
        name='novedades',
    ),
    path(
        'novedades/<slug:slug>',
        views.NewsView.as_view(),
        name='novedad',
    ),
]
