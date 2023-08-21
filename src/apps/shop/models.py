from django.db import models

# Create your models here.
class ShopModel(models.Model):
    owner = models.ForeignKey("users.UsersModel", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, null=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey("ShopModel", on_delete=models.SET_NULL, null=True, blank=True)
    specs = models.OneToOneField("ProductSpesificationModel", on_delete=models.CASCADE)
    preorder = models.OneToOneField("ProductPreorderModel", on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.name
    
class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=255)
    
class ProductVariationModel(models.Model):
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    variation_code = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self) -> str:
        return self.color

class ProductSpesificationModel(models.Model):
    brand = models.CharField(max_length=255, null=True, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)

class ProductPreorderModel(models.Model):
    preorder = models.BooleanField(default=False)
    sku = models.CharField(max_length=60)
    codition = models.CharField(max_length=20)