from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.views import APIView
# Create your views here.







class MostrarAPIUsuarios(ListAPIView):
    
    serializer_class = UsuarioSerializer
    pagination_class = UsuarioPagination
    def get_queryset(self):
        return Usuario.objects.all() 

class ModificarUsuario(RetrieveUpdateAPIView):
    serializer_class = ModificarUsuario
    def get_queryset(self):
        return Usuario.objects.all()

class MostrarAPIPersonal(RetrieveAPIView):
      
      def get_serializer_class(self):
          i = 1
          if i == 1:
              return DetallePersonal
          return DetalleInvitado

      def get_queryset(self):
        return Personal.objects.all()
          
# class MostrarAPIPersonal(RetrieveAPIView):
#     serializer_class = DetallePersonal
#     pagination_class = UsuarioPagination
#     def get_queryset(self):
#         return Personal.objects.all()

class MostrarAPIInvitado(RetrieveAPIView):
    serializer_class = DetalleInvitado
    pagination_class = UsuarioPagination
    def get_queryset(self):
        return Invitado.objects.all()



class CrearAPIUsuario(CreateAPIView):
    serializer_class = PeronalSerializer
    def get_queryset(self):
        return Personal.Objects.all()


class CrearAPIInvitado(CreateAPIView):
    serializer_class = InvitadoSerializer
    def get_queryset(self):
        return Invitado.objects.all()

class EditarAPIPersonal(RetrieveUpdateAPIView):
    serializer_class=EditarPersonal

    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validate_data.get('nombre')
            message = f'datos guardados {name}'
            return Response({'message':message})

    def get_queryset(self):
        return Personal.objects.all()


class EditarAPIInvitado(RetrieveUpdateAPIView):
    serializer_class =EditarInvitado
    def get_queryset(self):
        return Invitado.objects.all()

class EliminarUsuario(DestroyAPIView):
    serializer_class =  UsuarioSerializer
    def get_queryset(self):
        return Usuario.objects.all()


class UserAPI(APIView):
    def post(self,request):
        serializer = UsuarioPersonal(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

# class PaisSerializer(ApiView):









#     serializer_class = PaisSerializer
#     def get(self):

      