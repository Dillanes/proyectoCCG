from django.urls import path,include

from . import views 


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.loginEntrar,name='index'),
    path('logout/',views.logoutSalir, name="logout"),
    path('registrar/',views.registrarUsuario,name="registrarEmp"),
    path('menu/',views.MenuUsuario, name="menu"),
    path('registrarV/',views.registrarVisistante,name='registrarVis'),
    path('administrarU/',views.administrarUsuarios,name='adminUsers'),
    path('perfilUsuario/<pk>/<rol>/',views.PerfilUsuario, name ='PerfilUsuario'),
    path('Modificar/<int:id>/', views.EditarUser, name ='modificar'), 
    path('Eliminar/<int:id>/',views.EliminarUsuario,name ='eliminar'),
    path('Personal/',views.inicioPersonal,name='personal'),
    path('PerfilPersonal/',views.perfilPersonal,name='perfilPersonal'), #url de acceso   
    path('Invitado/',views.inicioInvitado,name='invitado'),
]