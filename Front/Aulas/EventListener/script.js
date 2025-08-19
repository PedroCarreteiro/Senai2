let btn = document.querySelector("button");

function random(num){
    return Math.floor(Math.random() * (num + 1));
}

// function bgChange (){
//     let cor = "rgb(" + random(255) + "," + random(255) + "," + random(255) + ")";
//     document.body.style.backgroundColor = cor;
// }

// btn.addEventListener("click", bgChange);

// //Função anônima
// btn.addEventListener("click", function (){
//     let cor = "rgb(" + random(255) + "," + random(255) + "," + random(255) + ")";
//     document.body.style.backgroundColor = cor;
// });

// //Função anônima arrow function
// btn.addEventListener("click", ()=>{
//     let cor = "rgb(" + random(255) + "," + random(255) + "," + random(255) + ")";
//     document.body.style.backgroundColor = cor;
// });

// //Botão troca de cor com event e target
// function bgChange(event){
//     let cor = "rgb(" + random(255) + "," + random(255) + "," + random(255) + ")";

//     event.target.style.backgroundColor = cor;
// }

// btn.addEventListener("click", bgChange)