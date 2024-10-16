from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "woo_search.utils"

    def ready(self):
        from . import checks  # noqa
