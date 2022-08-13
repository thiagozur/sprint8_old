from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Tarjetas
from Clientes.models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def tarjetas(request):
    userobj = get_object_or_404(User, username=request.user)
    uname = userobj.first_name
    usurname = userobj.last_name
    ufullname = uname[0] + usurname
    uid = userobj.username.split(ufullname)[1]
    clientobj = Cliente.objects.get(customer_id = uid)
    tarjetas = Tarjetas.objects.filter(customerid = clientobj.customer_id)
    return render(request, 'Tarjetas/tarjetas.html', {'name' : f'{userobj.first_name} {userobj.last_name[0]}', 'cards' : tarjetas})