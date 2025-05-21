"""
URL configuration for observador_digital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

# Importaciones del modulo de usuarios
from usuarios.views import registro_usuario, lista_usuarios, detalle_usuario, editar_usuario, eliminar_usuario, login_usuario, inicio, logout_usuario

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
    path("", inicio, name="inicio"),
    path("registro_usuario/", registro_usuario, name="registro_usuario"),
    path("usuarios/", lista_usuarios, name="lista_usuarios"),

    # Primary Key como parámetro:
    path("usuarios/<int:pk>/", detalle_usuario, name="detalle_usuario"),
    path("usuarios/<int:pk>/editar/", editar_usuario, name="editar_usuario"),
    path("usuarios/<int:pk>/eliminar/", eliminar_usuario, name="eliminar_usuario"),
]
