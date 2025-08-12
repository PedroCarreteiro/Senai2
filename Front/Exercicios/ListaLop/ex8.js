let lista = [];
let negativos = 0;

for(let i = 1; i <= 10; i++){
    let numero = prompt(`Digite o ${i}° número`);
    lista.push(numero);
}

for(let i = 0; i <= lista.length; i++){
    if(lista[i] < 0){
        negativos++;
    }
}

alert(`Temos ${negativos} números negativos na lista`);