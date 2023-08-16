from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from apps.users.manager import UserManager

# Create your models here.
class UsersModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    nama = models.CharField(unique=True, max_length=255)
    birth = models.DateField()
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone = PhoneNumberField(region="ID")
    shop = models.ForeignKey("shop", on_delete=models.SET_NULL, null=True, blank=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.email