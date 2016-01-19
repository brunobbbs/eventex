from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
