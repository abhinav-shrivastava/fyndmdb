from tastypie.resources import ModelResource
from api.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        excludes = ['created_at', 'updated_at']
