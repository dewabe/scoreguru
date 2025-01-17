from django.apps import AppConfig


class ScoreguruConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scoreguru'

    def ready(self):
        import scoreguru.signals