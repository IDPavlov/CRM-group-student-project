from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=256)


class CrmUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=Role.objects.get(name='seller'))

    def __str__(self):
        return self.username



class Product(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=12, decimal_places=2)


class BankAccount(models.Model):
    client = models.ForeignKey(CrmUser, on_delete=models.CASCADE)
    number = models.CharField(max_length=16, editable=False, unique=True)


class Deal(models.Model):
    client = models.ForeignKey(CrmUser, on_delete=models.PROTECT, related_name="client")
    seller = models.ForeignKey(CrmUser, on_delete=models.PROTECT, related_name="seller")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
