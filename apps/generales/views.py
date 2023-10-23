from django.views.generic import TemplateView

from .models import Logo, SliderHome
from apps.productos.models import Brand

class HomeView(TemplateView):
    template_name = 'front/home.html'

    def get_context_data(self, **kwargs):
        logo = Logo.objects.get(active=True)
        sliderHome = SliderHome.objects.filter(active=True)
        brands = Brand.objects.filter(active=True)
        context = {
            'logo': logo,
            'sliderHome': sliderHome,
            'brands': brands,
        }
        return context
