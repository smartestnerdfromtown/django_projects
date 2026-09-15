from django.apps import AppConfig

# ShortenerConfig will be used in settings.py to register the app.
# You register an app inside INSTALLED_APPS list.
class ShortenerConfig(AppConfig):
    name = 'shortener'