from django.urls import path
from .views import LogoutView, mostrariniciosesion, mostrarregistro, mostrarbienvenida, listarportafolio, crearportafolio, actualizarportafolio, eliminarportafolio
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

    path('', views.ip, name='mostrarpresentacion'),
    path('mostrariniciosesion/', mostrariniciosesion.as_view(), name='mostrariniciosesion'),
    path('accounts/login/', mostrariniciosesion.as_view(), name='mostrarsesion'),
    path('mostrarbienvenida/', mostrarbienvenida.as_view(), name='mostrarbienvenida'),
    path('mostrarregistro/', mostrarregistro.as_view(), name='mostrarregistro'),
    path('cerrarsesion/', LogoutView.as_view(), name='cerrarsesion'),

    path('listarportafolio/', listarportafolio.as_view(), name='listarportafolio'),

    path('crearportafolio/', login_required(crearportafolio.as_view()), name='crearportafolio'),
    path('actualizarportafolio/<int:pk>', login_required(actualizarportafolio.as_view()), name='actualizarportafolio'),
    path('eliminarportafolio/<int:pk>', login_required(eliminarportafolio.as_view()), name='eliminarportafolio'),
]