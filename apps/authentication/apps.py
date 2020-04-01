from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = 'apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        pass

