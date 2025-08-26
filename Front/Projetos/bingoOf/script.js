//Definir elementos
let btnSortear = document.getElementById("sortearNumero")
let btnReiniciar = document.getElementById("reiniciarJogo")

//Definir listas que serão utilizadas
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

//Função ativada quando a página é carregada, recarregada ou quando o botão de reiniciar é acionado. 
//Utilizada para iniciar/reiniciar o jogo
function iniciar() {
  //Deixar todas as listas vazias
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
  
  //Popular as listas de acordo com as letras BINGO
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

  //Popular a lista que contém as listas de números
  numeros.push(numerosB);
  numeros.push(numerosI);
  numeros.push(numerosN);
  numeros.push(numerosG);
  numeros.push(numerosO);

  //Esvaziar todas as colunas das letras BINGO e definir o número atual como "--"
  document.getElementById("listaNumerosB").innerHTML = ''

  document.getElementById("listaNumerosI").innerHTML = ''

  document.getElementById("listaNumerosN").innerHTML = ''

  document.getElementById("listaNumerosG").innerHTML = ''

  document.getElementById("listaNumerosO").innerHTML = ''

  document.getElementById("numeroAtual").textContent = "--";

  //Fazer uma lista que contém todos os números sem separação por letra BINGO
  listaFull = numeros.join()
  listaFull = listaFull.split(",")
}

//Função para sortear um novo número
btnSortear.onclick = function() {

  //Verificar se todos os números já foram sorteados, e se já foram, mandar um alert e já encerrar a função
  if(listaFull.length === 0){
    alert("Todos os números já foram sorteados!");
    return;
  }
  
  //Soertar um indice da lista de números que não foram sorteados e pegar o número que está nesse índice
  const indice = Math.floor(Math.random() * listaFull.length);
  const numero = listaFull[indice];  

  //Adicionar o numero na lista de sorteados e remove-lo da lista de números não sorteados
  sorteados.push(numero);
  listaFull.splice(indice, 1);

  //Verificar em qual letra BINGO o número se adequa e adicionar esse número a lista de sorteados da letra correspondente tanto no JS como na coluna correspondente no HTML
  //Além de imprimir o número sorteado junto com sua letra de acordo com a sua letra BINGO na seção de número sorteado
  if(numero >= 1 && numero <= 15){
    sorteadosB.push(numero)
    document.getElementById("listaNumerosB").innerHTML = 
    sorteadosB.map(num => `<article id="num${num}">${num}</article>`).join("");
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

//Chamar a função de iniciar caso o botão de reiniciar seja acionado
btnReiniciar.onclick = function reiniciar() {
  iniciar();
}

//Iniciar a função iniciar no carregamento da página
iniciar();