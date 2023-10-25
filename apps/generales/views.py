from django.views.generic import TemplateView

from .models import Logo, SliderHome, GalleryHome, SocialNetwork, Videos, Statistic, Us
from apps.productos.models import Brand


class HomeView(TemplateView):
    template_name = 'front/home.html'

    def get_context_data(self, **kwargs):
        try:
          logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
          logo = None
        sliderHome = SliderHome.objects.filter(active=True)
        brands = Brand.objects.filter(active=True)
        try:
          galleryHome = GalleryHome.objects.get(active=True)
        except GalleryHome.DoesNotExist:
          galleryHome = None
        videos = Videos.objects.filter(active=True)
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'sliderHome': sliderHome,
            'brands': brands,
            'galleryHome': galleryHome,
            'videos': videos,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context


class UsView(TemplateView):
    template_name = 'front/nosotros.html'

    def get_context_data(self, **kwargs):
        try:
          logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
          logo = None
        items = Us.objects.filter(active=True)
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'items': items,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context
