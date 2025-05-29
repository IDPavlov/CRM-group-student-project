from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

Client = get_user_model()


class Job(models.Model):
    name = models.CharField(max_length=256)


class Worker(AbstractUser):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=12, decimal_places=2)


class BankAccount(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number = models.CharField(max_length=16, editable=False, unique=True)


class Deal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    seller = models.ForeignKey(Worker, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

# TODO: СВОЙ USERMANAGER ДЛЯ КЛАССА Worker (ЧТОБЫ ЕГО МОЖНО БЫЛО ИСПОЛЬЗОВАТЬ)