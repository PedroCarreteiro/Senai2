// const totalNumeros = 75;
// let numeros = [];
// let sorteados = [];

// function iniciar() {
//   numeros = [];
//   sorteados = [];
//   for (let i = 1; i <= totalNumeros; i++) {
//     numeros.push(i);
//   }
//   //Map para executar a cada elemento do array e o join para juntar todas essas mini divs em um comando só (programação 2)
//   document.getElementById("listaNumeros").innerHTML = numeros.map(num => `<div id="num${num}">${num}</div>`).join("");
//   document.getElementById("numeroAtual").textContent = "--";
// }

// function sortearNumero() {
//   if (numeros.length === 0) {
//     alert("Todos os números já foram sorteados!");
//     return;
//   }
//   const indice = Math.floor(Math.random() * numeros.length);
//   const numero = numeros[indice];

//   sorteados.push(numero);
//   numeros.splice(indice, 1);

//   document.getElementById("numeroAtual").textContent = numero;
//   document.getElementById("num" + numero).classList.add("sorteado");
// }

// function reiniciar() {
//   iniciar();
// }

// iniciar();



// Quantidade total de números possíveis no bingo (1 até 75)
const totalNumeros = 75;

// Array que guarda os números que AINDA PODEM ser sorteados
let numeros = [];

// Array que guarda os números que JÁ FORAM sorteados (histórico)
let sorteados = [];

/**
 * Função responsável por iniciar (ou reiniciar) o estado do bingo.
 * - Preenche o array `numeros` de 1 até `totalNumeros`
 * - Limpa o histórico `sorteados`
 * - Constrói a grade visual com todos os números
 * - Reseta o visor do "número atual"
 */
function iniciar() {
  // Garante que começamos com arrays vazios
  numeros = [];
  sorteados = [];

  // Preenche `numeros` com 1, 2, 3, ..., totalNumeros
  for (let i = 1; i <= totalNumeros; i++) {
    numeros.push(i);
  }

  // Monta o HTML com uma <div> para cada número e injeta tudo de uma vez
  ////Map para executar a cada elemento do array e o join para juntar todas essas mini divs em um comando só (programação 2)
  // - cada número recebe um id único "numX" (ex: num23) para podermos marcar depois
  document.getElementById("listaNumeros").innerHTML =
    numeros.map(num => `<div id="num${num}">${num}</div>`).join("");

  // Reseta o display do último número sorteado para "--"
  document.getElementById("numeroAtual").textContent = "--";
}

/**
 * Sorteia um número aleatório entre os que ainda não foram sorteados.
 * - Evita repetições removendo o número do array `numeros`
 * - Atualiza o visor com o número sorteado
 * - Marca visualmente o número sorteado na lista
 */
function sortearNumero() {
  // Se não há mais números disponíveis, informa e sai da função
  if (numeros.length === 0) {
    alert("Todos os números já foram sorteados!");
    return; // interrompe a função aqui
  }

  //
  // Gera um índice aleatório válido dentro do array `numeros`
  // Math.random() -> [0, 1)
  // Multiplica pelo tamanho do array para distribuir no intervalo correto
  // Math.floor(...) para "arredondar para baixo" e obter um índice inteiro
  const indice = Math.floor(Math.random() * numeros.length);

  // Pega o número na posição sorteada
  const numero = numeros[indice];

  // Adiciona o número ao histórico de sorteados
  sorteados.push(numero);

  // Remove o número do array de disponíveis para evitar repetição
  // splice(indice, 1) remove exatamente 1 elemento na posição `indice`
  numeros.splice(indice, 1);

  // Mostra o número sorteado no visor principal
  document.getElementById("numeroAtual").textContent = numero;

  // Encontra a caixinha correspondente (ex: id="num23") e marca como "sorteado"
  // Isso aplica a classe CSS .sorteado para mudar a cor/estilo
  document.getElementById("num" + numero).classList.add("sorteado");
}

/**
 * Reinicia o jogo chamando `iniciar()` novamente.
 * - Útil para limpar tudo e começar um novo sorteio
 */
function reiniciar() {
  iniciar();
}

// Ao carregar o script/página, inicializa tudo para deixar pronto para uso
iniciar();