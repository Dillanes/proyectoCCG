//BOTON DE MOSTRAR CONTRASEÑA
const pass = document.querySelector('.item-password');
const mostrarpassw = document.querySelector('.bt-mostrarPass');
//CONSTANTES PARA VALIDAR EL FORMULARIO
const formularioEmpleado = document.querySelector('#fomularioE');
const nombre = document.querySelector('#id_nombre');
const paterno = document.querySelector('#id_paterno');
const materno = document.querySelector('#id_materno');
const fnacimiento = document.querySelector('#id_fechanac').value;
const lnacimiento = document.querySelector('#id_lugarnac');
const rfc = document.querySelector('#id_rfc');
const curp = document.querySelector('#id_curp');
const telefono = document.querySelector('#id_cel');
const calle = document.querySelector('#id_calle');
const noint = document.querySelector('#id_noint');
const noext = document.querySelector('#id_noext');
const cp = document.querySelector('#item_cp');
const usuario = document.querySelector('#idusername');
let aceptado = /^[0-9]+$/;
let correo_regex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;


(function(){ formularioEmpleado.addEventListener('submit',(e)=>{
       
     //VARIABLES
       let nombreV = String(nombre.value).trim();
       let paternoV = String(paterno.value).trim();
       let maternoV = String(materno.value).trim(); 
       let lnacimientoV = String(lnacimiento.value).trim();
       let rfcV = String(rfc.value).trim();
       let curpV = String(curp.value).trim();
       let telefonoV = String(telefono.value).trim();
       let calleV = String(calle.value).trim();
       let nointV = String(noint.value).trim();
       let noextV = String(noext.value).trim();
       let cpV = String(cp.value).trim();
       let usuarioV = String(usuario.value).trim();
       let passV = String(pass.value).trim();
     
     //CONDICIONES

      if(nombreV.length == 0 || nombreV.length < 3){
          alert("nombre no valido");
          e.preventDefault();
      }else if(paternoV.length == 0 || paternoV.length <3){
          alert('Apellido paterno no valido');
          e.preventDefault();
      }else if(maternoV.length == 0 || maternoV.length <3){
          alert("Apellido materno no valido");
          e.preventDefault();
      }else if(!document.querySelector('input[name="genero"]:checked')){
           alert('Seleccione su genero');
           e.preventDefault();
      }else if(fnacimiento==null){
           alert('Fecha no valida');
           e.preventDefault();
      }else if(lnacimientoV.length == 0 || lnacimientoV.length<5){
           alert('Lugar de nacimiento no valido');
           e.preventDefault();
      }else if(rfcV.length!=13){
          alert('RFC no valido');
          e.preventDefault();
     }else if(curpV.length!=18){
          alert('CURP no valida');
          e.preventDefault();
     }else if(telefonoV.length!=10 || !(telefonoV.match(aceptado))){
          alert('Telefono no valido');
          e.preventDefault();
     }else if(calleV.length == 0 || calleV.length<3){
          alert('Calle no valida');
          e.preventDefault();
     }else if(!(nointV.match(aceptado) || noint.length<2)){
          alert('Numero no valido');
          e.preventDefault();
     }else if(!(noextV.match(aceptado))|| noextV.length<2){
          alert('Numero exterior no valido');
          e.preventDefault()
     }else if(!(cpV.match(aceptado))|| cpV.length<4){
          alert('Codigo Postal no valido');
          e.preventDefault();
     }else if(!(correo_regex.test(usuarioV))){
          alert("La dirección de email " + usuarioV + " es incorrecta");
          e.preventDefault();
     }else if(passV.length<4){
          alert('La contraseña es demasiada corta');
          e.preventDefault();
     }
     })
})();

(function(){
     mostrarpassw.addEventListener('click',()=>{
          if(pass.type == 'password'){
               pass.type = 'text';
          }else{
              pass.type = 'password';
          }
     });
})();

$(function() {
     $('#id_rfc').focusout(function() {
         // Uppercase-ize contents
         this.value = this.value.toLocaleUpperCase();
     });
 });

 $(function() {
     $('#id_curp').focusout(function() {
         // Uppercase-ize contents
         this.value = this.value.toLocaleUpperCase();
     });
 });