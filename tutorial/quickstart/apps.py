from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorial.quickstart'

    def ready(self):
        import tutorial.quickstart.signals