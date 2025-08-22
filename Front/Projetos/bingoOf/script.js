let numerosB = [];
let numerosI = [];
let numerosN = [];
let numerosG = [];
let numerosO = [];
let numeros = [];
let sorteados = [];
let sorteadosB = [];
let sorteadosI = [];
let sorteadosN = [];
let sorteadosG = [];
let sorteadosO = [];
let listaFull = [];

function iniciar() {
  numerosB = [];
  numerosI = [];
  numerosN = [];
  numerosG = [];
  numerosO = [];
  numeros = [];
  sorteados = [];
  sorteadosB = [];
  sorteadosI = [];
  sorteadosN = [];
  sorteadosG = [];
  sorteadosO = [];
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
  // document.getElementById("listaNumerosB").innerHTML = 
  // numerosB.map(num => `<article id="num${num}">${num}</article>`).join("");

  // document.getElementById("listaNumerosI").innerHTML = 
  // numerosI.map(num => `<article id="num${num}">${num}</article>`).join("");

  // document.getElementById("listaNumerosN").innerHTML = 
  // numerosN.map(num => `<article id="num${num}">${num}</article>`).join("");

  // document.getElementById("listaNumerosG").innerHTML = 
  // numerosG.map(num => `<article id="num${num}">${num}</article>`).join("");

  // document.getElementById("listaNumerosO").innerHTML = 
  // numerosO.map(num => `<article id="num${num}">${num}</article>`).join("");

  document.getElementById("listaNumerosB").innerHTML = ''

  document.getElementById("listaNumerosI").innerHTML = ''

  document.getElementById("listaNumerosN").innerHTML = ''

  document.getElementById("listaNumerosG").innerHTML = ''

  document.getElementById("listaNumerosO").innerHTML = ''


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


  if(numero >= 1 && numero <= 15){
    sorteadosB.push(numero)
    document.getElementById("listaNumerosB").innerHTML = 
    sorteadosB.map(num => `<article id="num${num}">${num}</article>`).join("");
    // document.getElementById("listaNumerosB").innerHTML = `<article id="num${numero}">${numero}</article>`
    document.getElementById("numeroAtual").textContent = "B"+numero;
  }
  else if (numero >= 16 && numero <= 30){
    sorteadosI.push(numero)
    document.getElementById("listaNumerosI").innerHTML = 
    sorteadosI.map(num => `<article id="num${num}">${num}</article>`).join("");
    document.getElementById("numeroAtual").textContent = "I"+numero;
  }
  else if(numero >= 31 && numero <= 45){
    sorteadosN.push(numero)
    document.getElementById("listaNumerosN").innerHTML = 
    sorteadosN.map(num => `<article id="num${num}">${num}</article>`).join("");
    document.getElementById("numeroAtual").textContent = "N"+numero;
  }
  else if(numero >= 46 && numero <= 60){
    sorteadosG.push(numero)
    document.getElementById("listaNumerosG").innerHTML = 
    sorteadosG.map(num => `<article id="num${num}">${num}</article>`).join("");
    document.getElementById("numeroAtual").textContent = "G"+numero;
  }
  else if(numero >= 61 && numero <= 75){
    sorteadosO.push(numero)
    document.getElementById("listaNumerosO").innerHTML = 
    sorteadosO.map(num => `<article id="num${num}">${num}</article>`).join("");
    document.getElementById("numeroAtual").textContent = "O"+numero;
  }
}

function reiniciar() {
  iniciar();
}

iniciar();