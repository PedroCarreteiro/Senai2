const lis = document.querySelector('#idlistinea')

fetch('http://localhost:8000/listar_filmes_mari').then((res) => {
    return res.json();
}).then((data) => {
    data.map((lista) => {
        console.log(lista)
        lis.innerHTML += `
        <li>
            <strong>Nome do Filme: <strong/> ${lista.nome} </br>
            <strong>Atores: <strong/> ${lista.atores} </br>
            <strong>Diretor: <strong/> ${lista.diretor} </br>
            <strong>Ano de Lançamento: <strong/> ${lista.ano_lancamento} </br>
            <strong>Genero: <strong/> ${lista.genero} </br>
            <strong>Produtora: <strong/> ${lista.produtora} </br>
            <strong>Sinopse: <strong/> ${lista.sinopse} </br>
            <button id="btnExcluir">Excluir</button>
        <li/>
        `
    })
})

