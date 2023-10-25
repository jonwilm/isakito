from django.views.generic import TemplateView, DetailView

from .models import Brand, SliderBrand, Product
from apps.generales.models import Logo, SocialNetwork, Statistic


class BrandsView(TemplateView):
    template_name = 'front/marcas.html'

    def get_context_data(self, **kwargs):
        try:
          logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
          logo = None
        brands = Brand.objects.filter(active=True)
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'brands': brands,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context


class BrandView(DetailView):
    model = Brand
    template_name = 'front/marca.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        try:
          logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
          logo = None
        sliderBrand = SliderBrand.objects.filter(brand=brand, active=True)
        products = Product.objects.filter(brand=brand, active=True)
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'brand': brand,
            'logo': logo,
            'sliderBrand': sliderBrand,
            'products': products,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context
