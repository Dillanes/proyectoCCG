from rest_framework import serializers, pagination
from .models import *



class DetallePersonal(serializers.ModelSerializer):
      class Meta:
            model = Personal
            fields = ('idpersonal','nombre','paterno','materno','genero','fechanac','lugarnac','rfc','curp','cel','calle','noint','noext')


class DetalleInvitado(serializers.ModelSerializer):
      class Meta:
            model = Invitado
            fields = ('idinvitado','nombre','paterno','materno','cargo','cel','orgprocedencia','descripcion')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
      relacion_usuario = DetallePersonal(many=True, read_only=True,default=True)
      relacion_usuarioI = DetalleInvitado(many=True, read_only=True,default=False)
      delete_User = serializers.HyperlinkedIdentityField(view_name='crudapi_app:EliminarUsuario',lookup_field='pk')
      UpdateUsuario = serializers.HyperlinkedIdentityField(view_name='crudapi_app:EditarUsuario', lookup_field='pk')
      class Meta:
            model = Usuario
            fields = ('idusuario','username','password','rol','fechacreacion','fechaact','delete_User','UpdateUsuario','relacion_usuario','relacion_usuarioI')
            extra_kwargs = {
                  'password':{
                    'write_only':True,
                    'style':{'input_type':'password'}
                  }
            }


class UsuarioPagination(pagination.PageNumberPagination):
      page_size = 5
      max_page_size = 50



class PeronalSerializer(serializers.ModelSerializer):
      class Meta:
            model= Personal
            fields =('nombre','paterno','materno','genero','fechanac','lugarnac','rfc','curp','cel','calle','noint','noext')

class InvitadoSerializer(serializers.ModelSerializer):
      class Meta:
            model= Invitado
            fields = ('nombre','paterno','materno','cargo','cel','orgprocedencia','descripcion')


class EditarPersonal(serializers.ModelSerializer):
      class Meta:
            model=Personal
            fields =('idpersonal','nombre','paterno','materno','genero','fechanac','lugarnac','rfc','curp','cel','calle','noint','noext')

class EditarInvitado(serializers.ModelSerializer):
      class Meta:
            model = Invitado
            fields = ('idinvitado','nombre','paterno','materno','cargo','cel','orgprocedencia','descripcion')

class ModificarUsuario(serializers.ModelSerializer):
      class Meta:
            model = Usuario
            fields = ('username','password')
            extra_kwargs = {
                  'password':{
                        'style':{'input_type':'password'},}
            }

'''CREAR USUARIOS PARA PERSONAL Y INVITADO'''

class UsuarioPersonal(serializers.Serializer):
      idpersonal = serializers.ReadOnlyField()
      nombre = serializers.CharField()
      paterno = serializers.CharField()
      materno = serializers.CharField()
      genero = serializers.CharField()
      fechanac = serializers.DateField()
      lugarnac = serializers.CharField()
      rfc = serializers.CharField()
      curp = serializers.CharField()
      cel = serializers.CharField()
      calle = serializers.CharField()
      noint = serializers.IntegerField()
      noext = serializers.IntegerField()
      username = serializers.CharField()
      password = serializers.CharField()


      def create(self,validate_data):
           personal = Personal()
           usuario  = Usuario()

           usuario.username = validate_data.get('username')
           usuario.password = validate_data.get('password')
           new_usuario = usuario.save(commit=False)

           personal.nombre = validate_data.get('nombre')
           personal.paterno = validate_data.get('paterno')
           personal.materno = validate_data.get('materno')
           personal.genero = validate_data.get('genero')
           personal.fechanac = validate_data.get('fechanac')
           personal.lugarnac = validate_data.get('lugarnac')
           personal.rfc = validate_data.get('rfc')
           personal.curp = validate_data.get('curp')
           personal.cel = validate_data.get('cel')
           personal.calle = validate_data.get('calle')
           personal.noint = validate_data.get('noint')
           personal.noext = validate_data.get('noext')
           personal.fk_cp = 3104
           personal.fk_usuario = new_usuario.idusuario

           new_usuario.save()
           personal.save()

      def validate_username(self,data):
            usuario = Usuario.objects.filter(username=data).exists()
            if usuario:
                  raise serializers.ValidationError('Este usuario ya existe')
            else:
                  return data




   

