import json

from tastypie.resources import ModelResource, ALL
from api.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        excludes = ['created_at', 'updated_at']
        filtering = {
            'name': ALL,
        }

    def dehydrate(self, bundle):
      # We deserialize the genre field here. If it's null we return empty array
      bundle.data['genre'] = json.loads(bundle.data['genre']) if bundle.data['genre'] else []
      return bundle
