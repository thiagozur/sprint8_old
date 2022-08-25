"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Clientes.models import Cliente
from rest_framework import routers, serializers, viewsets,  permissions
from rest_framework.permissions import SAFE_METHODS

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'customer_id',
            'customer_name',
            'customer_surname',
            'customer_dni',
            'dob',
            'branch_id',
            'tipo',
        ]

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]

router = routers.DefaultRouter()
router.register(r'clientes', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Clientes.urls', namespace='Clientes')),
    path('accounts/', include('Cuentas.urls', namespace='Cuentas')),
    path('tarjetas/', include('Tarjetas.urls', namespace='Tarjetas')),
    path('prestamos/', include('Prestamos.urls', namespace='Prestamos')),
    path('', include('Login.urls', namespace='Login')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
