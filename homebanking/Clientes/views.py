from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    userobj = get_object_or_404(User, username=request.user)
    return render(request, 'Clientes/home.html', {'name' : f'{userobj.first_name} {userobj.last_name[0]}'})