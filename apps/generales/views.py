from django.views.generic import TemplateView

from .models import Logo, SliderHome, GalleryHome, Videos
from apps.productos.models import Brand

class HomeView(TemplateView):
    template_name = 'front/home.html'

    def get_context_data(self, **kwargs):
        logo = Logo.objects.get(active=True)
        sliderHome = SliderHome.objects.filter(active=True)
        brands = Brand.objects.filter(active=True)
        try:
          galleryHome = GalleryHome.objects.get(active=True)
        except GalleryHome.DoesNotExist:
          galleryHome = None
        videos = Videos.objects.filter(active=True)
        context = {
            'logo': logo,
            'sliderHome': sliderHome,
            'brands': brands,
            'galleryHome': galleryHome,
            'videos': videos,
        }
        return context
