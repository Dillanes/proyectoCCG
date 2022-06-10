const btactive = document.querySelector('.icon-bar');
const listoptions = document.querySelector('.ul-list');

btactive.addEventListener('click',()=>{
    listoptions.classList.toggle('ul-list-active')
})