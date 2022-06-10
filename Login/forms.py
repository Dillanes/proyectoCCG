from django.forms import ModelForm
from .models import Usuario,Personal,Usuario,Invitado
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



CHOICES=[('H','Hombre'),
         ('M','Mujer')]


# 1.-FORMULARIO DEL LOGIN
class FormularionLogin(ModelForm):
    class Meta: 
        model = Usuario
        fields = ('username','password')
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}),
            'password': forms.TextInput(attrs={'type':'password','placeholder':'Contraseña'})
        }
    # class Meta:
    #    model = Usuario
    #    fields =   ('username','password',)

    #    widgets = {
    #        'username': forms.TextInput(attrs={'placeholder':'example@prueba.com', 'id':'idusername', 'name':'idusername', 'class':'item-mail'}),
    #        'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña...', 'class':'item-password', 'id':'id_password'})
    #    }

    #    labels = {
    #        'correo':'Correo',
    #        'password': 'Contraseña'
    #    }


    # def clean(self):
    #     username = self.cleaned_data['username'] 
    #     password = self.cleaned_data['password']

    #     if not authenticate(username = username, password = password):
    #         raise forms.validationError("Usuario o contraseña incorrecta")
    


#2.-FORMULARIO DE EL PERSONAL
class FormularioPersonal(ModelForm):
    class Meta:
     model = Personal
     
    #  fields = ('nombre','materno','paterno','genero','fechanac','lugarnac','rfc','curp','cel','noint','noext','fk_usuario','fk_cp')

     fields = ('nombre','paterno','materno','genero','fechanac','lugarnac','rfc','curp','cel','calle','noint','noext','fk_usuario','fk_cp')
     
     widgets = {
         'nombre': forms.TextInput(attrs={'placeholder':'Nombre..',}),
         'paterno': forms.TextInput(attrs={'placeholder':'Apellido paterno..',}),
         'materno': forms.TextInput(attrs={'placeholder':'Apellido materno..',}),
         'rfc': forms.TextInput(attrs={'placeholder':'RFC..',}),
         'curp': forms.TextInput(attrs={'placeholder':'CURP..',}),
         'lugarnac': forms.TextInput(attrs={'placeholder':'Lugar de nacimiento..',}),
         'calle': forms.TextInput(attrs={'placeholder':'Calle..',}),
         'noint': forms.TextInput(attrs={'placeholder':'Numero interior..',}),
         'noext': forms.TextInput(attrs={'placeholder':'Numero exterior..',}),
        'fechanac' : forms.DateInput(attrs={'type': 'date',}),
        'genero' : forms.RadioSelect(choices = CHOICES, attrs={'class':'Boton-radio'}),
        'fk_cp' : forms.HiddenInput(),
        'cel' : forms.TextInput(attrs={'type':'number','placeholder':'Tel..'}),
    }


# 3.- FORMULARIO DIRECCION


# 4.- FORMULARIO DEL USUARIO
class FormulariUsuario(ModelForm):
    class Meta:
     model = Usuario
     fields = ('idusuario','username','password','rol')

     labels = {
           'correo':'Correo',
           'password': 'Contraseña'
       }
     
     widgets = {
           'username': forms.TextInput(attrs={'placeholder':'example@prueba.com', 'id':'idusername', 'name':'idusername', 'class':'item-mail'}),
           'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña...', 'class':'item-password', 'id':'id_password'}),
           'rol': forms.HiddenInput(attrs={'value':'Empleado'}),
    
           
       }

class FormularioInvitado(ModelForm):
      class Meta:
            model = Invitado
            fields = '__all__'
        
            widgets = {
            'descripcion': forms.Textarea(attrs={'placeholder':'description.....'}),
            'nombre': forms.TextInput(attrs={'placeholder':'Name..'}),
            'paterno': forms.TextInput(attrs={'placeholder':'Apellido Paterno'}),
            'materno': forms.TextInput(attrs={'placeholder':'Apellido Materno..'}),
            'cargo': forms.TextInput(attrs={'placeholder':'Cargo..'}),
            'cel': forms.TextInput(attrs={'placeholder':'Telefono..', 'type':'number'}),
            'orgprocedencia': forms.TextInput(attrs={'placeholder':'Organizacion de procedencia..'}),
            }

class formUser(ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','password','rol')
        
