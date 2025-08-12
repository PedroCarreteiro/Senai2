function random(num){
    return Math.floor(Math.random() * (num + 1));
}

let infinito = function (){
    let cor = "rgb(" + random(255) + "," + random(255) + "," + random(255) + ")";
    document.body.style.backgroundColor = cor;
}

// for(let i = 0; i < 10; i++){
//     setTimeout(infinito, 1000);
// }

const intervalId = setInterval(infinito, 100);

setTimeout(() => {
    clearInterval(intervalId);
    alert("Aacabou")
}, 100000);