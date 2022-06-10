// SELECTORES 

const formularioVisita = document.querySelector('#formularioVisita');
const btpass = document.querySelector('#mostrarpass')
const txtnombre = document.querySelector('#id_nombre');
const txtpaterno = document.querySelector('#id_paterno');
const txtmaterno = document.querySelector('#id_materno');
const txtcargo = document.querySelector('#id_cargo');
const txtnumero = document.querySelector('#id_cel');
const txtorgprocedencia = document.querySelector('#id_orgprocedencia');
const txtcp = document.querySelector('#item_cp');
const txtusuario = document.querySelector('#idusername')
const txtpassword = document.querySelector('#id_password')
const txttextarea = document.querySelector('#id_descripcion');
let aceptado = /^[0-9]+$/;
let regex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
//EVENTO DE FORMULARIO


     
    (function(){ formularioVisita.addEventListener('submit',(e)=>{
    
        //VARIABLES
        let nombre = String(txtnombre.value).trim();
        let paterno = String(txtpaterno.value).trim();
        let materno = String(txtmaterno.value).trim();
        let cargo = String(txtcargo.value).trim();
        let numero = String(txtnumero.value).trim();
        let cp = String(txtcp.value).trim();
        let org = String(txtorgprocedencia.value).trim();
        let usuario = String(txtusuario.value).trim();
        let password = String(txtpassword.value).trim();
        let textarea = String(txttextarea.value).trim();
        
            //CONDICIONES
            if(nombre.length == 0 || nombre.length < 3){
                alert("nombre no valido");
                e.preventDefault();
                
            }else if(paterno.length == 0 || paterno.length <3){
                alert('Apellido paterno no valido');
                e.preventDefault();
            }else if(materno.length == 0 || materno.length <3){
                alert("Apellido materno no valido");
                e.preventDefault();
            }else if(cargo.length == 0 || cargo.length < 3){
                alert('cargo no valido');
                e.preventDefault();
            }else if(!numero.match(aceptado) || numero.length < 10){
                alert('telefono no valido');
                e.preventDefault();
            }else if(org.length == 0 || org.length<3){
                alert('campo organizacion de procedencia invalida');
                e.preventDefault();
            }else if (!cp.match(aceptado) || cp.length <4 ){
                alert('Direccion invalida, seleccione su codigo postal');
                e.preventDefault();
            }else if (!(regex.test(usuario))){
                alert("La dirección de email " + usuario + " es incorrecta");
                e.preventDefault();
               }else if(password.length<4){
                alert("Contraseña muy corta")
               }else if(textarea.length<10){
                     alert('Descripcion demasiada corta')
                     e.preventDefault();
               }
            
        });
    })();

    (function(){
            btpass.addEventListener('click',()=>{
                if(txtpassword.type == 'password'){
                    txtpassword.type='text';
                }else{
                    txtpassword.type='password';
                }
            })
        }
    )();
        

       