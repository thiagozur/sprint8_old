from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login as dlogin
from Clientes.models import Cliente
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                dlogin(request, user)
                url = request.GET.get('next')
                if url is not None:
                    return HttpResponseRedirect(url)
                else:
                    return HttpResponseRedirect('home/')
            else:
                loginform = LoginForm()
                loginform.fields['username'].widget.attrs['placeholder'] = 'Usuario o contraseña incorrectos'
                loginform.fields['password'].widget.attrs['placeholder'] = 'Usuario o contraseña incorrectos'
                return render(request, 'Login/login.html', {'loginform' : loginform})       
    else:
        loginform = LoginForm()
    return render(request, 'Login/login.html', {'loginform' : loginform})

def createclients(request):
    clients = Cliente.objects.all()
    for i in clients:
        nuser = User.objects.create_user(username = f'{i.customer_name[0]}{i.customer_surname}{i.customer_id}', password = i.customer_dni, email = f'{i.customer_name[0]}{i.customer_surname}@gmail.com', first_name = i.customer_name, last_name = i.customer_surname)
        nuser.save()
    return HttpResponse('<h1>Usuarios creados</h1>')