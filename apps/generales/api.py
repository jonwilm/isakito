from django.conf import settings
from tastypie.resources import ModelResource
from .models import PuntoDeVenta


class PuntoDeVentaResource(ModelResource):
    
    def dehydrate(self, bundle):
        del bundle.data['coordenadas']
        bundle.data['lat'] = bundle.obj.coordenadas.y
        bundle.data['lng'] = bundle.obj.coordenadas.x
        return bundle

    class Meta:
        queryset = PuntoDeVenta.objects.all()
        resource_name = 'generales'
        list_allowed_methods = ['get']
        filtering = {
            'localidad': ('exact', ),
        }
        max_limit = None
