from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models import signals
from tastypie.models import create_api_key

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
       # Dispatch signal to Tastypie for creating APIKey whenever a user is
       # created
       signals.post_save.connect(create_api_key, sender=User)
