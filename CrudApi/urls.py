from django.urls import path
from .views import * 


app_name = 'crudapi_app'
urlpatterns=[
    path('api/ListaUsuarios/',MostrarAPIUsuarios.as_view(), name='ListarUsuarios'),
    path('api/CrearUsuario/',CrearAPIUsuario.as_view(),name='CrearUsuario'),
    path('api/CrearInvitado/' ,CrearAPIInvitado.as_view(), name='CrearInvitado'),
    path('api/ModificarPersonal/<pk>/',EditarAPIPersonal.as_view(),name='ModificarPersonal'),
    path('api/ModificarInvitado/<pk>/',EditarAPIInvitado.as_view(),name='ModificarInvitado'),
    path('api/DetallePersonal/<pk>/', MostrarAPIPersonal.as_view(),name='DetallePersonal'),
    path('api/DetalleInvitado/<pk>/',MostrarAPIInvitado.as_view(),name = 'DetalleInvitado'),
    path('api/EliminarUsuario/<pk>/',EliminarUsuario.as_view(), name = 'EliminarUsuario'),
    path('api/ModificarUsuario/<pk>',ModificarUsuario.as_view(), name = 'EditarUsuario'),
    path('api/AddUser/', UserAPI.as_view(),name='addUser'),
]