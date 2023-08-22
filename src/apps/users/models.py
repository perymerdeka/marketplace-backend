from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from apps.users.manager import UserManager
from apps.users.validators import AccountNumberValidator

# Create your models here.
class UsersModel(AbstractBaseUser, PermissionsMixin):
    nama = models.CharField(unique=True, max_length=255)
    birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone = PhoneNumberField(region="ID")


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class PaymentMethodModel(models.Model):
    default_payment = models.BooleanField(default=False)
    holder_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=30, validators=[AccountNumberValidator])
    bank = models.ForeignKey("bank.BankModel", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.account_number