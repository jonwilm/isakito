from django.urls import path

from .register import register_models

from .views import PanelIndexView, PanelAppsView

urlpatterns = [
  path('', PanelIndexView.as_view(), name='panel-index'),
  path('<str:app>', PanelAppsView.as_view(), name='panel-apps'),
]

urlpatterns += register_models()
