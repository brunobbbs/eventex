from django.db import models


class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    phone = models.CharField('Telefone', max_length=12)
    email = models.EmailField('Email')
    created_at = models.DateTimeField('Inscrito em', auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'inscrito'
        verbose_name_plural = 'inscritos'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name