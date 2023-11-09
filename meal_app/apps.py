from django.apps import AppConfig


class MealAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meal_app'

    def ready(self):
        import meal_app.signals
