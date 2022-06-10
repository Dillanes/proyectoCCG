from django.shortcuts import render,redirect, get_object_or_404
from .forms import FormularionLogin,FormularioPersonal,FormulariUsuario,FormularioInvitado,formUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Usuario,Pais,Estado,Mundeleg,Cp,Personal,Invitado
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError
from django.utils import timezone
from datetime import datetime

def inicio(request):
    return render(request,'inicio.html',)


# def home(request):
#       message = None
#       if request.method == 'POST':
#          form = LoginForm(request.POST)
#          print(form.errors)
#          if form.is_valid():
#             message = "holaaa"
#             username = request.POST['username']
#             password =  request.POST['password']
#             user = Usuario.objects.get(username)
#             passw = Usuario.objects.get(password)
#             user = authenticate(username=user,password=passw)
#             if user is not None:
#                if user.is_active:
#                   login(request,user)
#                   message = "Te haz identificado de modo correcto"
#                else:
#                   message = "Tu usuario esta inactivo"
#             else:
#                message = "Nombre de usuario o contraseña incorrecta"
#       else:
#          form = LoginForm()
      
#       return render(request,'registration/login.html',{'form':form,'message':message},)
def logoutSalir(request):
    estado = request.session['estatus']
    ide = request.session['idusuario']
    DelEstado = Usuario.objects.get(idusuario = ide)
    DelEstado.estatus = 0
    DelEstado.save()
    
    if Personal.objects.filter(fk_usuario=ide).exists():
       del request.session['idpersonal']
       del request.session['usernameP']
       del request.session['username']
       del request.session['estatus']
       del request.session['idusuario']
       
    elif Invitado.objects.filter(fk_usuario=ide).exists():
       del request.session['usernameI']
       del request.session['idinvitado']
       del request.session['username']
       del request.session['estatus']
       del request.session['idusuario']

    messages.info(request, 'Saliste exitosamente')
    return redirect('index')

  
def loginEntrar(request): 
      if request.method == 'POST':
           form = FormularionLogin(request.POST)
           if form.is_valid():
              usuario = request.POST.get('username')
              contrasena = request.POST.get('password')
              option = Usuario.objects.filter(username=usuario,password=contrasena).exists()
              if option:
                 new_usuario = Usuario.objects.get(username=usuario,password=contrasena)
                 request.session['username'] = new_usuario.username
                 request.session['estatus'] = new_usuario.estatus
                 request.session['idusuario'] = new_usuario.idusuario
                 request.session['rol'] = new_usuario.rol
                 usuarioLogeado = Usuario.objects.get(username=usuario)
                 usuarioLogeado.fechaact = timezone.now()
                 usuarioLogeado.estatus = 1
                 usuarioLogeado.save()

                 if usuarioLogeado.rol == 'Empleado':
                    new_usuarioPersonal = Personal.objects.get(fk_usuario = new_usuario.idusuario)
                    request.session['idpersonal'] =  new_usuarioPersonal.idpersonal
                    request.session['usernameP'] = new_usuarioPersonal.nombre
                    return redirect('personal')

                 elif usuarioLogeado.rol == 'Visitante':
                    new_usuarioInvitado = Invitado.objects.get(fk_usuario = new_usuario.idusuario)
                    request.session['idinvitado'] =  new_usuarioInvitado.idinvitado
                    request.session['usernameI'] = new_usuarioInvitado.nombre
                    return redirect('invitado')

              else:
                 messages.warning(request,'Usuario o contraseña incorrecta')
      form = FormularionLogin()
      name = Usuario.objects.values('username')
      return render(request,'registration/login.html',{'form':form,'name':name})




def MenuUsuario(request):
      return render(request,'menu.html')

      
def registrarUsuario(request):
        pais = Pais.objects.all()
        estado = Estado.objects.all()
        municipio = Mundeleg.objects.all()
        cp = Cp.objects.all()
        message = None
        

        if request.method == 'POST':
             formU = FormulariUsuario(request.POST)
             formP = FormularioPersonal(request.POST)
             print(formP.errors)
             if formU.is_valid() and formP.is_valid():
                new_formP = formP.save(commit=False)
                new_formU = formU.save(commit = False)
                new_formU.rol = 'Empleado'
                value_cp = request.POST.get('cp')
                new_formP.fk_cp = value_cp
                value_username = request.POST.get('username')
                userN = Usuario.objects.filter(username=value_username).exists()
                if userN:
                    messages.warning(request,'El usuario '+value_username+' ya se encuentra registrado')
                else:
                  new_formU.save()
                  print(formP.errors)
                  new_formP.fk_usuario = new_formU.idusuario
                  print(formP.errors)
                  new_formP.save()
                  messages.success(request, 'Bienvenido '+value_username) 
                  return redirect('registrarEmp')
             else:
                  messages.warning(request, 'Ha ocuurido un error.')
        else:
              formU = FormulariUsuario()
              formP = FormularioPersonal()
        return render(request,'RegistroEmpleado.html',{'pais':pais,'estado':estado,'municipio':municipio, 'cp': cp,'formU':formU,'formP':formP},)

def registrarVisistante(request):
      pais = Pais.objects.all()
      estado = Estado.objects.all()
      municipio = Mundeleg.objects.all()
      cp = Cp.objects.all()
      if request.method == 'POST':
            formV = FormularioInvitado(request.POST)
            formU = FormulariUsuario(request.POST)
            print('***************')
            print(formV.errors)
            print('***************')
            if formV.is_valid() and formU.is_valid():
                 new_formV = formV.save(commit=False)
                 new_formU = formU.save(commit=False)
                 new_formU.rol = 'Visitante'
                 value_mun = request.POST.get('mundeleg')
                 new_formV.fk_mundeleg = value_mun
                 value_username = request.POST.get('username')
                 userN = Usuario.objects.filter(username=value_username).exists()
                 if userN:
                    messages.warning(request,'El usuario '+value_username+' ya se encuentra registrado')
                 else:
                  new_formU.save()
                  new_formV.fk_usuario = new_formU.idusuario
                  print(formV.errors)
                  new_formV.save()
                  messages.success(request, 'Bienvenido '+value_username) 
                  return redirect('registrarVis')     
            else:
                 messages.warning(request, 'Ha ocuurido un error.')
      else:
         formU = FormulariUsuario()
         formV = FormularioInvitado()

              
      return render(request,'RegistroVisitante.html',{'pais':pais,'estado':estado,'municipio':municipio, 'cp': cp,'formU':formU,'formV':formV},)



def administrarUsuarios(request):
      usuarios = Usuario.objects.exclude(rol ='Admin')
      
      contexto={
         'usuarios':usuarios,
          }
      return render(request,'AdministrarUsuarios.html',contexto)



def EditarUser(request,id):
      user = get_object_or_404(Usuario,idusuario=id)
      data={
         'form':formUser(instance=user),
      }

      if request.method=='POST':
         formulario = formUser(data=request.POST, instance=user, files = request.FILES)
         if formulario.is_valid():
            formulario.save()
            messages.success(request,'La modificacion se realizo correctamente')
         else:
            message.warning(request,'La modificacion no se pude realizar')
         data['form'] = formulario
      return render(request,'Crud/AdminEditar.html',data)


def EliminarUsuario(request,id):
     usern = get_object_or_404(Usuario, idusuario = id)
     user = Usuario.objects.get(idusuario=id)
     
     if user.rol == 'Empleado':
        personal = get_object_or_404(Personal,fk_usuario=id)
        personal.delete()
        usern.delete()

     elif user.rol == 'Visitante':
        visitante = get_object_or_404(Invitado,fk_usuario=id)
        visitante.delete()
        user.delete()

     return redirect ('adminUsers')


def inicioPersonal(request):
   return render(request,'Personal/inicioPersonal.html')


def perfilPersonal(request):
   ID = request.session['idpersonal']
   ID2 = request.session['idusuario']
   userP = get_object_or_404(Personal,idpersonal=ID)
   userU = get_object_or_404(Usuario,idusuario=ID2)
   data={
      'formP':FormularioPersonal(instance=userP),
      'formU':formUser(instance=userU)
   }

   if request.method == 'POST':
       formularioP = FormularioPersonal(data=request.POST, instance=userP, files=request.FILES)
       formularioU = formUser(data=request.POST, instance=userU, files=request.FILES)
       if formularioP.is_valid() and formularioU.is_valid():
          
          formularioP.save()
          formularioU.save()
          messages.success(request,'La modificacion se llevo con exito')
       else:
          messages.warning(request,'No se pudo realizar la modificacion')
       data['formP'] = formularioP
       data['formU'] = formularioU
   return render(request,'Personal/perfilPersonal.html',data)

def inicioInvitado(request):
   return render(request,'Invitado/inicioInvitado.html')

def PerfilUsuario(request,pk,rol):

    if rol == 'Empleado':
       personal = Personal.objects.get(fk_usuario=pk)
       return render(request,'perfinUsuario.html',{'personal':personal})
    elif rol == 'Visitante':
       invitado = Invitado.objects.get(fk_usuario=pk)
       return render(request,'perfinUsuario.html',{'invitado':invitado})

    messages.warning(request,'Ocurrio un herror')
