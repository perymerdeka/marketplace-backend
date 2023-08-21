from django.contrib import admin
from django.apps import apps

from apps.shop.models import *

# Register your models here.

class ShopModelAdmin(admin.ModelAdmin):
    pass

class ProductModelAdmin(admin.ModelAdmin):
    pass

class ProductCategoryModelAdmin(admin.ModelAdmin):
    pass

class ProductSpesificationModelAdmin(admin.ModelAdmin):
    pass

class ProductPreoderModelAdmin(admin.ModelAdmin):
    pass
class ProductVariationModelAdmin(admin.ModelAdmin):
    pass

# iterate here

models_class = apps.get_app_config("shop").get_models()

model_admin = [ShopModelAdmin, ProductModelAdmin, ProductVariationModelAdmin, ProductCategoryModelAdmin]


for model in models_class:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass