from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('contacto/', views.contacto),
    path('cursos/', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('cursos/edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('cursos/eliminarCurso/<codigo>', views.eliminarCurso)
]