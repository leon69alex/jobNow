# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def __str__(self):
    return self.nom

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    adreca = models.CharField(max_length=250)
    nif = models.CharField(max_length=8)
    #oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE,)

