const totalNumeros = 75;
let numeros = [];
let sorteados = [];

function iniciar() {
  numeros = [];
  sorteados = [];
  for (let i = 1; i <= totalNumeros; i++) {
    numeros.push(i);
  }
  //Map para executar a cada elemento do array e o join para juntar todas essas mini divs em um comando só (programação 2)
  document.getElementById("listaNumeros").innerHTML = numeros.map(num => `<div id="num${num}">${num}</div>`).join("");
  document.getElementById("numeroAtual").textContent = "--";
}

function sortearNumero() {
  if (numeros.length === 0) {
    alert("Todos os números já foram sorteados!");
    return;
  }
  const indice = Math.floor(Math.random() * numeros.length);
  const numero = numeros[indice];

  sorteados.push(numero);
  numeros.splice(indice, 1);

  document.getElementById("numeroAtual").textContent = numero;
  document.getElementById("num" + numero).classList.add("sorteado");
}

function reiniciar() {
  iniciar();
}

iniciar();
