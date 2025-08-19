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
  numerosB.map(num => `<div id="num${num}">${num}</div>`).join("");

  document.getElementById("listaNumerosI").innerHTML = 
  numerosI.map(num => `<div id="num${num}">${num}</div>`).join("");

  document.getElementById("listaNumerosN").innerHTML = 
  numerosN.map(num => `<div id="num${num}">${num}</div>`).join("");

  document.getElementById("listaNumerosG").innerHTML = 
  numerosG.map(num => `<div id="num${num}">${num}</div>`).join("");

  document.getElementById("listaNumerosO").innerHTML = 
  numerosO.map(num => `<div id="num${num}">${num}</div>`).join("");


  document.getElementById("numeroAtual").textContent = "--";

}

function sortearNumero() {

  //numerosB.length === 0 || numerosI.length === 0 || numerosN.length === 0 || numerosG.length === 0 || numerosO.length === 0


  

  const indice = Math.floor(Math.random() * numeros.length);
  const lista = numeros[indice];
  



  const numeroIndice = Math.floor(Math.random() * lista.length);
  const numero = lista[numeroIndice];

  
  if(sorteados.includes(numero)){
    alert("Todos os números já foram sorteados!");
    return;
  }

  sorteados.push(numero);

  console.log(lista)
  console.log(numero)
  

  lista.splice(numeroIndice, 1);
  console.log(lista)
  console.log(sorteados)

  

  if(indice == 0){
    document.getElementById("numeroAtual").textContent = "B"+numero;
  }
  else if(indice == 1){
    document.getElementById("numeroAtual").textContent = "I"+numero;
  }
  else if(indice == 2){
    document.getElementById("numeroAtual").textContent = "N"+numero;
  }
  else if(indice == 3){
    document.getElementById("numeroAtual").textContent = "G"+numero;
  }
  else if(indice == 4){
    document.getElementById("numeroAtual").textContent = "O"+numero;
  }

  document.getElementById("num" + numero).classList.add("sorteado");
}

function reiniciar() {
  iniciar();
}

iniciar();