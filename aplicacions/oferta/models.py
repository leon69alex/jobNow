# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from aplicacions.empresa.models import Empresa

class Oferta(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,)
    capcalera = models.TextField()
    descripcio = models.TextField()
    horari = models.TextField()
    dataPublicacio = models.DateTimeField(auto_now=True)
    CategoriaChoices = (
        ("0", "Administració d'empreses"),
        ("1", "Administració pública"),
        ("2", "Atenció al client"),
        ("3", "I+D"),
        ("4", "Magatzem"),
        ("5", "Disseny i arts gràfiques"),
        ("6", "Educació"),
        ("7", "Banca"),
        ("8", "Informàtica"),
        ("9", "Telecomunicacions"),
        ("10", "Ingenier tècnic"),
        ("11", "Immobiliaria"),
        ("12", "Advocacia"),
        ("13", "Marketing"),
        ("14", "Altres"),
        ("15", "Art"),
        ("16", "RRHH"),
        ("17", "Sanitat"),
        ("18", "Sector farmaceutic"),
        ("19", "Turisme"),
        ("20", "Restauració"),
    )
    categoria = models.CharField(
        max_length=100,
        choices = CategoriaChoices,
    )
    publicada = models.BooleanField(default=False)
