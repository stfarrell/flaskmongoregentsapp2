console.log('connected')
let ansBtn = document.querySelector('#ansBtn');
let ansDiv = document.querySelector('#ansDiv');
let randomAns = '{{ randomAns }}';
let currentVid = document.querySelector('#currentVid');
let vidBtn = document.querySelector('#vidBtn');


vidBtn.addEventListener('click', e=>{
    console.log('Good job clicking!');
    currentVid.classList.toggle('hide');
});

ansBtn.addEventListener('click', e=>{
    console.log('Great job clicking!');
    ansDiv.classList.toggle('hide');
})