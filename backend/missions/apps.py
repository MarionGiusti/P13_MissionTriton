from django.apps import AppConfig


class MissionsConfig(AppConfig):
    name = 'missions'

    def ready(self):
        import missions.signals
