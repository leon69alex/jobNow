from django.shortcuts import render, redirect
from .forms import  LoginForm
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout)
from django.contrib import messages
from aplicacions.oferta.models import Oferta

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
                    messages.error(request,"Usuari o password incorrecte o usuari no actiu")
                    return redirect("portal:index")
    else:
        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'index.html', ctx)