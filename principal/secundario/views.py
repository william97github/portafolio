from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from .models import portafolio
from .forms import portafolioforms, registrofroms

from django.shortcuts import render
from ipware import get_client_ip

import sqlite3

# Create your views here.
def ip(request):
    if request.method=="GET":
        client_ip, is_routable = get_client_ip(request)
        conexion = sqlite3.connect('db.portafolio')
        conexion.execute("insert into secundario_ips(ip,enrutable) values (?,?)", (f"{client_ip}", f"{is_routable}"))
        conexion.commit()
        conexion.close()
    return render(request, 'presentacion.html')

class mostrarbienvenida(ListView):
    model = portafolio
    template_name = ('bienvenida.html')
    def get_queryset(self, *args, **kwargs):
        lista = portafolio.objects.filter(autor=self.request.user)
        return lista

class mostrariniciosesion(LoginView):
    template_name = ('iniciosesion.html')

class listarportafolio(ListView):
    model = portafolio
    queryset = portafolio.objects.all()
    template_name = ('listarportafolio.html')
    paginate_by = 6

class crearportafolio(CreateView):
    model = portafolio
    form_class = portafolioforms
    template_name = ('crearportafolio.html')
    success_url = '/'

class actualizarportafolio(UpdateView):
    model = portafolio
    form_class = portafolioforms
    template_name = ('crearportafolio.html')
    success_url = '/'

class eliminarportafolio(DeleteView):
    model = portafolio
    success_url = '/'

class mostrarregistro(CreateView):
    form_class = registrofroms
    template_name = ('registrousuario.html')
    success_url = '/'

