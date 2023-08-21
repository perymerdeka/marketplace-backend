from django.contrib import admin

from django.apps import apps
# Register your models here.


models_name = apps.get_app_config("bank").get_models()

for model in models_name:
    admin.site.register(model)