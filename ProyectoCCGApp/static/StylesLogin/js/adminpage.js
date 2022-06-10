menuadmin = document.querySelector('.icon-bar');
mostrarmenu = document.querySelector('.lista-admin');

menuadmin.addEventListener('click',()=>{
    mostrarmenu.classList.toggle("lista-on");
})