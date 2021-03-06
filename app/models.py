from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from scripts.token_generator import generate_token
from datetime import datetime
from vizitcard.settings import STATIC_ROOT


class User(AbstractUser):
    worker = models.OneToOneField('Worker', on_delete=models.CASCADE, null=True, default=None)
    avatar = models.ImageField(default='img/avatars/default_avatar.png', upload_to='img/avatars/')
    biography = models.TextField(null=True)
    location = models.TextField(null=True)


class Card(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    telegram = models.TextField()
    vk = models.TextField()
    whats_app = models.TextField()
    telephone = models.TextField()
    url = models.CharField(max_length=30)
    serialized_array = models.TextField()


class File(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    path = models.FileField()
    icon = models.FileField()


class Organization(models.Model):
    creator = models.OneToOneField(User, null=True, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    activated = models.BooleanField(default=False)

    card = models.OneToOneField(Card, null=True, on_delete=models.SET_NULL)


class Worker(models.Model):
    position = models.TextField(default="", editable=False)
    work_card = models.OneToOneField(Card, null=True, default=None, on_delete=models.SET_NULL)
    org = models.OneToOneField(Organization, null=True, default=None, on_delete=models.SET_NULL)


class Token(models.Model):
    token = models.CharField(max_length=30, default=generate_token, null=False)
    token_type = models.CharField(max_length=30, default='activation')
    creation_date = models.DateTimeField(default=timezone.now)
    lifetime = models.IntegerField(default=1)
    user = models.OneToOneField(to=User, blank=True, null=True, on_delete=models.PROTECT)


class OrganizationToken(Token):
    org = models.OneToOneField(Organization, on_delete=models.CASCADE)
