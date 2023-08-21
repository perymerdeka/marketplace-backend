from django.contrib import admin

# Register your models here.

from django.apps import apps

apps_models = apps.get_app_config("users").get_models()

for model in apps_models:
    admin.site.register(model)