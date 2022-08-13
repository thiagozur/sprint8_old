from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Cliente
from Cuentas.models import Cuenta
from Tarjetas.models import Tarjetas

# Create your views here.

def home(request):
    userobj = get_object_or_404(User, username=request.user)
    uname = userobj.first_name
    usurname = userobj.last_name
    ufullname = uname[0] + usurname
    uid = userobj.username.split(ufullname)[1]
    clientobj = Cliente.objects.get(customer_id = uid)
    cuentas = Cuenta.objects.filter(customer_id = clientobj.customer_id)
    tarjetas = Tarjetas.objects.filter(customerid = clientobj.customer_id)
    return render(request, 'Clientes/home.html', {'name' : f'{userobj.first_name} {userobj.last_name[0]}', 'accounts' : cuentas, 'cards' : tarjetas})