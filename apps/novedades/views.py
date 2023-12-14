from django.views.generic import TemplateView, DetailView

from .models import News
from apps.generales.models import Logo, SocialNetwork, Statistic, Catalogo


class NewsListView(TemplateView):
    template_name = 'front/novedades.html'

    def get_context_data(self, **kwargs):
        try:
          logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
          logo = None
        try:
            catalogo = Catalogo.objects.get(active=True)
        except Catalogo.DoesNotExist:
            catalogo = None
        newsList = News.objects.filter(active=True).order_by('date_created')
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'catalogo': catalogo,
            'newsList': newsList,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context


class NewsView(DetailView):
    model = News
    template_name = 'front/novedad.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = self.get_object()
        try:
          logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
          logo = None
        try:
            catalogo = Catalogo.objects.get(active=True)
        except Catalogo.DoesNotExist:
            catalogo = None
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'news': news,
            'logo': logo,
            'catalogo': catalogo,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context