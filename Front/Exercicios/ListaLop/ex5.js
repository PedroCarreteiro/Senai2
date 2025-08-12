let numero = prompt("Digite um número: ");

while(numero <= 0){
    alert("Número inválido!");
    numero = prompt("Digite um número: ");
}

for(let i = 1; i <= numero; i++){
    console.log(i);
}

