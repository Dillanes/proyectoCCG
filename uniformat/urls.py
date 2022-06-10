from django.urls import path

from . import views

urlpatterns = [
    path('', views.nivel1, name="Uniformat"),
    path('UFTNivel2/<int:nivel1_id>', views.nivel2, name="nivel2"),
    path('UFTNivel3/<int:nivel2_id>/<int:nivel_ant>', views.nivel3, name="nivel3"),
    path('UFTNivel4/<int:nivel3_id>/<int:nivel_ant>/<int:nivel_ant_ant>', views.nivel4, name="nivel4"),
    path('agregarCaregoria', views.agregarCategoria, name="agregarCategoria"),
    path('eliminarCategoria/<int:id>', views.eliminarCategoria, name="eliminarCategoria"),
    path('editarCategoria/<int:id>', views.editarCategoria, name="editarCategoria"),
    path('agregarNivel2/<int:nivel1_id>', views.agregarNivel2, name="agregarNivel2"),
    path('eliminarNivel2/<int:id>/<int:nivel1_id>', views.eliminarNivel2, name="eliminarNivel2"),
    path('editarNivel2/<int:id>/<int:nivel1_id>', views.editarNivel2, name="editarNivel2"),
    path('agregarNivel3/<int:nivel2_id>/<int:nivel1_id>', views.agregarNivel3, name="agregarNivel3"),
    path('eliminarNivel3/<int:id>/<int:nivel2_id>/<int:nivel1_id>', views.eliminarNivel3, name="eliminarNivel3"),
    path('editarNivel3/<int:id>/<int:nivel2_id>/<int:nivel1_id>', views.editarNivel3, name="editarNivel3"),
    path('agregarNivel4/<int:nivel3_id>/<int:nivel2_id>/<int:nivel1_id>', views.agregarNivel4, name="agregarNivel4"),
    path('eliminarNivel4/<int:id>/<int:nivel3_id>/<int:nivel2_id>/<int:nivel1_id>', views.eliminarNivel4, name="eliminarNivel4"),
    path('editarNivel4/<int:id>/<int:nivel3_id>/<int:nivel2_id>/<int:nivel1_id>', views.editarNivel4, name="editarNivel4"),

]