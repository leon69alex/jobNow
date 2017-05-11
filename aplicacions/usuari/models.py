# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from aplicacions.oferta.models import Oferta

class Usuari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    cognoms = models.CharField(max_length=200)
    naixement = models.DateField(null=True)
    dni = models.CharField(max_length=9)
    adreca = models.CharField(max_length=250)
    poblacio = models.CharField(max_length=50)
    cp = models.CharField(max_length=5, default=12345)
    nif = models.CharField(max_length=8)
    estudis = models.TextField()
    idiomes = models.TextField()
    ofertesPreferides = models.ForeignKey(Oferta, on_delete=models.CASCADE,)
    imatge = models.ImageField(upload_to='perfil/', default='perfil/default.gif')


@receiver(post_save, sender=Usuari)
def create_user_usuari(sender, instance, created, **kwargs):
    if created:
        Usuari.objects.create(user=instance)

@receiver(post_save, sender=Usuari)
def save_user_usuari(sender, instance, **kwargs):
    instance.profile.save()
# Create your models here.
