let numerosB = [];
let numerosI = [];
let numerosN = [];
let numerosG = [];
let numerosO = [];
let numeros = [];
let sorteados = [];
let listaFull = [];

function iniciar() {
  numerosB = [];
  numerosI = [];
  numerosN = [];
  numerosG = [];
  numerosO = [];
  numeros = [];
  sorteados = [];
  listaFull = [];
  
  for (let i = 1; i <= 15; i++) {
    numerosB.push(i);
  }
  for (let i = 16; i <= 30; i++) {
    numerosI.push(i);
  }
  for (let i = 31; i <= 45; i++) {
    numerosN.push(i);
  }
  for (let i = 46; i <= 60; i++) {
    numerosG.push(i);
  }
  for (let i = 61; i <= 75; i++) {
    numerosO.push(i);
  }

  numeros.push(numerosB);
  numeros.push(numerosI);
  numeros.push(numerosN);
  numeros.push(numerosG);
  numeros.push(numerosO);

  //Map para executar a cada elemento do array e o join para juntar todas essas mini divs em um comando só (programação 2)
  document.getElementById("listaNumerosB").innerHTML = 
  numerosB.map(num => `<article id="num${num}">${num}</article>`).join("");

  document.getElementById("listaNumerosI").innerHTML = 
  numerosI.map(num => `<article id="num${num}">${num}</article>`).join("");

  document.getElementById("listaNumerosN").innerHTML = 
  numerosN.map(num => `<article id="num${num}">${num}</article>`).join("");

  document.getElementById("listaNumerosG").innerHTML = 
  numerosG.map(num => `<article id="num${num}">${num}</article>`).join("");

  document.getElementById("listaNumerosO").innerHTML = 
  numerosO.map(num => `<article id="num${num}">${num}</article>`).join("");


  document.getElementById("numeroAtual").textContent = "--";

  listaFull = numeros.join()
  listaFull = listaFull.split(",")

}

function sortearNumero() {


  if(listaFull.length === 0){
    alert("Todos os números já foram sorteados!");
    return;
  }

  console.log(listaFull)
  
  const indice = Math.floor(Math.random() * listaFull.length);
  const numero = listaFull[indice];  

  sorteados.push(numero);
  listaFull.splice(indice, 1);

  

  // if(indice == 0){
  //   document.getElementById("numeroAtual").textContent = "B"+numero;
  // }
  // else if(indice == 1){
  //   document.getElementById("numeroAtual").textContent = "I"+numero;
  // }
  // else if(indice == 2){
  //   document.getElementById("numeroAtual").textContent = "N"+numero;
  // }
  // else if(indice == 3){
  //   document.getElementById("numeroAtual").textContent = "G"+numero;
  // }
  // else if(indice == 4){
  //   document.getElementById("numeroAtual").textContent = "O"+numero;
  // }


  if(numero >= 1 && numero <= 15){
    document.getElementById("numeroAtual").textContent = "B"+numero;
  }
  else if (numero >= 16 && numero <= 30){
    document.getElementById("numeroAtual").textContent = "I"+numero;
  }
  else if(numero >= 31 && numero <= 45){
    document.getElementById("numeroAtual").textContent = "N"+numero;
  }
  else if(numero >= 46 && numero <= 60){
    document.getElementById("numeroAtual").textContent = "G"+numero;
  }
  else if(numero >= 61 && numero <= 75){
    document.getElementById("numeroAtual").textContent = "O"+numero;
  }

  document.getElementById("num" + numero).classList.add("sorteado");
}

function reiniciar() {
  iniciar();
}

iniciar();