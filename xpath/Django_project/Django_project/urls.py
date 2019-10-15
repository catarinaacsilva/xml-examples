"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views

urlpatterns = [
    #path('cursos/', views.show_cursos, name='cursos'),
    path('', views.index),
    path('actionUrl', views.show_cursos),
    path('detalhe', views.show_details),
    path('filter_grau', views.show_grau),
    path('filter_dep', views.show_departamento),
    path('filter_area', views.show_areacientifica),
    path('filter_local', views.show_local),
    path('infoDep', views.all_departamentos),
    path('infoArea', views.all_areascientificas),
    path('infoLocal', views.all_locals),
    path('more_info_curso', views.more_info_curso)
]
