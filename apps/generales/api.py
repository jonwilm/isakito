from django.conf import settings
from tastypie.resources import ModelResource
from .models import PointOfSale


class PointOfSaleResource(ModelResource):
    
    def dehydrate(self, bundle):
        del bundle.data['coordinates']
        bundle.data['lat'] = bundle.obj.coordinates.y
        bundle.data['lng'] = bundle.obj.coordinates.x
        return bundle

    class Meta:
        queryset = PointOfSale.objects.all()
        resource_name = 'generales'
        list_allowed_methods = ['get']
        filtering = {
            'locality': ('exact', ),
        }
        max_limit = None
