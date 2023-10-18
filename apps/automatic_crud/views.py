from django.conf import settings
from django.apps import apps
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .forms import PanelLoginForm


class PanelLoginView(FormView):
    template_name = 'panel/login.html'
    form_class = PanelLoginForm
    success_url = reverse_lazy('panel-index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(PanelLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(PanelLoginView, self).form_valid(form)


class PanelIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        applications = []
        search = self.request.GET.get('q', '')
        for app in list(apps.app_configs.keys()):
            if 'apps.'+app in settings.LOCAL_APPS:
                if search != '' and search.lower() in app:
                    applications.append({
                        'name': app.replace('_', ' '),
                        'verbose_name': apps.get_app_config(app).verbose_name,
                        'real_name': app,
                    })
                elif search == '':
                    applications.append({
                        'name': app.replace('_', ' '),
                        'verbose_name': apps.get_app_config(app).verbose_name,
                        'real_name': app,
                    })
        context['applications'] = applications
        return context
    

class PanelAppsView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/apps.html'

    def get_context_data(self, **kwargs):
        context = {}
        app = apps.get_app_config(self.kwargs['app'])
        models = []
        search = self.request.GET.get('q', '')
        for model in app.get_models():
            if search != '' and search.lower() in model.__name__.lower():
                models.append({
                    'name': model.__name__.lower(),
                    'real_name': model.__name__
                })
            elif search == '':
                models.append({
                    'name': model.__name__.lower(),
                    'real_name': model.__name__
                })
        context['models'] = models
        context['app'] = self.kwargs['app']
        return context
    
