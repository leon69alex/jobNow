# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import  LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout)
from django.contrib import messages
from aplicacions.oferta.models import Oferta
from django.forms import modelform_factory
from aplicacions.usuari.models import Usuari
from django.db import IntegrityError

# def index(request):
#     return render(request, "index.html")

def index(request):
    if request.method=='POST':
        form=LoginForm( request.POST )
        if form.is_valid():
            user=authenticate( username = form.cleaned_data['username'],
                               password = form.cleaned_data['password'])
            if user and user.is_active:
                #si tot es ok:
                authLogin(request,user)
                totesOfertes = Oferta.objects.all().order_by('-id')[:5]
                ctx = {'ofertes': totesOfertes}
                #print user.name
                #return redirect('portal:index')
                return render(request, 'index.html', ctx)

            else:
                messages.error(request,"Usuari o password incorrecte")
                return redirect("portal:index")
    else:
        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'index.html', ctx)

def registre(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            user = User(
                    username = form.cleaned_data['username']

            )
        else:
            form = modelform_factory(User, fields=("username", "password", "email", "first_name", "last_name"))
            ctx = {'form': form,}
            return render(request, 'registre.html', ctx)

def logout(request):
    authLogout(request)
    return redirect('portal:index')
# def registre(request):
#     if not request.user.is_authenticated():
#         if request.method=='POST':
#             try:
#                 form=RegistrationForm( request.POST)
#                 if form.is_valid():
#                     #Procés creació usuari Models Propi
#                     user = Usuari(
#                         nomusuari=form.cleaned_data['username'],
#                         nom=form.cleaned_data['nom'],
#                         cognoms=form.cleaned_data['cognoms'],
#                         poblacio=form.cleaned_data['poblacio'],
#                         adreca=form.cleaned_data['adreca'],
#                         correu=form.cleaned_data['correu'],
#                         cp=form.cleaned_data['cp'],
#                         naixement=form.cleaned_data['naixement'],
#                         contrasenya=form.cleaned_data['password1'],
#                         authuser= None
#                     )
#                     user.save()
#                     messages.success(request, "T'has registrat correctament.")
#                     #Redirect
#                     return redirect('portal:login')
#                 else:
#                     messages.error(request, "Les dades son incorrectes")
#                     # Redirect
#                     return redirect('portal:registre')
#             except IntegrityError:
#                 messages.error(request, "Aquest nom d'usuari ja existeix. Prova'n un altre.")
#                 return redirect('portal:registre')
#         else:
#             form = RegistrationForm()
#             ctx = {'form': form, 'capcelera': "Formulari de Registre"}
#             return render(request, 'registre.html', ctx)
#     else:
#         return redirect('portal:index')