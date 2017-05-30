# -*- coding: utf-8 -*-
from django import forms
from aplicacions.usuari.models import Usuari
from django.forms.extras.widgets import SelectDateWidget
from functools import partial
from django_select2.forms import Select2Widget
#from aplicacions.llibres.models import Llibre

class LoginForm(forms.Form):
    username = forms.CharField(max_length=16,
                             help_text="Nom d'usuari.",widget=forms.TextInput(attrs={'placeholder': "Nom d'Usuari"}))
    password = forms.CharField(max_length=24,
                             help_text="Insereix la teva contrasenya",
                             widget=forms.PasswordInput(attrs={'placeholder': "Contrasenya"}),
                             )

class RegistrationForm(forms.Form) :
    username = forms.CharField(max_length=16,
                               help_text="Nom d'usuari.",
                               widget=forms.TextInput(
                                   attrs={'placeholder': "Nom d'Usuari"}
                               )
                               )
    password1 = forms.CharField(max_length=24,
                                help_text="Insereix la teva contrasenya",
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': "Contrasenya", 'pattern': '(?=^.{8,}$)((?=.*\\d)|(?=.*\\W+))(?![.\\n])(?=.*[A-Z])(?=.*[a-z]).*$'}
                                ),
                                )
    password2 = forms.CharField(max_length=24,
                                help_text="Repeteix la contrasenya",
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': "Repeteix la contrasenya", 'pattern': '(?=^.{8,}$)((?=.*\\d)|(?=.*\\W+))(?![.\\n])(?=.*[A-Z])(?=.*[a-z]).*$'}
                                )
                                )
    correu = forms.EmailField(max_length=30,
                              help_text="Insereix el teu correu",
                              widget=forms.EmailInput(
                                  attrs={'placeholder': "Correu electronic"}
                              )
                              )