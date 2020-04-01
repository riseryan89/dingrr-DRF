from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = 'dingrr.apps.auth'
    label = 'auth'
    verbose_name = 'Authentication'

    def ready(self):
        pass

default_app_config = 'apps.auth.AuthAppConfig'