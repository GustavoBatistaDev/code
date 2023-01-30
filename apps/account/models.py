from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


class ContatoAjuda(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        unique_together = [['usuario', 'email']]
