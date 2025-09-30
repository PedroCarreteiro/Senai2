const lis = document.querySelector('#idlistinea')

//Passar o ID na URL
async function irParaEdicao(id) {
    //Redirecionar para a página de edição
    window.location.href = `editar.html?id=${id}`;
}

//Obter parâmetros da URL
function getFilmeUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

//Carregar o filme e preencher o formulário com os dados que já tem
async function carregarDadosParaEdicao() {
    const filmeId = getFilmeUrl();
    const form = document.getElementById('form-edicao');

    if (!form || !filmeId) {
        //Não está na página de edição ou o ID está faltando
        return; 
    }

    //Get de todos os filmes e do específico
    try {
        const response = await fetch('http://localhost:8000/listar_filmes');
        if (!response.ok) throw new Error('Falha ao carregar a lista de filmes.');
        
        const filmes = await response.json();
        const filme = filmes.find(f => String(f.id) === filmeId);

        if (!filme) {
            alert("Filme não encontrado!");
            window.location.href = 'listar_filmes.html';
            return;
        }

        //Preencher os campos do formulário com os dados atuais
        document.getElementById('filme-nome-atual').textContent = filme.nome; 
        document.getElementById('filme-id').value = filmeId;
        
        document.getElementById('nome').value = filme.nome || '';
        document.getElementById('atores').value = filme.atores || '';
        document.getElementById('diretor').value = filme.diretor || '';
        document.getElementById('ano_lancamento').value = filme.ano_lancamento || '';
        document.getElementById('genero').value = filme.genero || '';
        document.getElementById('produtora').value = filme.produtora || '';
        document.getElementById('sinopse').value = filme.sinopse || '';

        //Enviar formulário
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            //Pegar dados do formulário
            const formData = new FormData(e.target);
            const dadosPatch = {};
            
            //Criar o json pra enviar
            for (const [key, value] of formData.entries()) {
                //Não fazer patch do id
                if (key !== 'filme-id') { 
                    dadosPatch[key] = value.trim();
                }
            }

            //Enviar patch
            enviarPatch(filmeId, dadosPatch);
        });

    //Caso haja erro
    } catch (error) {
        console.error("Erro ao carregar dados de edição:", error);
        alert("Não foi possível carregar os dados para edição.");
        window.location.href = 'listar_filmes.html';
    }
}

//Executa o recarregamento
document.addEventListener('DOMContentLoaded', carregarDadosParaEdicao);


//Função para enviar o patch
async function enviarPatch(id, dadosPatch) {
    
    //URL para os dados do patch
    fetch(`http://localhost:8000/filmes_mari/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(dadosPatch)
    })
    //Alerta e redirecionento de sucesso
    .then(response => {
        if (response.ok) {
            alert(`Filme ID ${id} atualizado com sucesso!`);
            
            window.location.href = 'listar_filmes.html'; 
            
        } else {
            alert('Erro ao tentar atualizar o filme. Verifique o servidor.');
        }
    })
    //Caso de erro
    .catch(error => {
        console.error('Erro na requisição PATCH:', error);
        alert('Erro de conexão ao tentar atualizar.');
    });
}


//Delete
async function deletarFilme(id) {
    //Confirmar deleção
    if (!confirm(`Tem certeza que deseja excluir o filme com ID ${id}?`)) {
        return;
    }

    //URl de transição de dados
    fetch(`http://localhost:8000/filmes_mari/${id}`, {
        method: 'DELETE'
    })
    //Alerta e reload de sucesso
    .then(response => {
        if (response.ok) {
            alert(`Filme ${id} excluído com sucesso!`);
            
            window.location.reload(); 
            
        } else {
            alert('Erro ao tentar excluir o filme.');
        }
    })
    //Caso aconteça um erro 
    .catch(error => {
        console.error('Erro na requisição DELETE:', error);
        alert('Erro de conexão ao tentar excluir.');
    });
}


//Caregara página de listar filmes com os jsons
fetch('http://localhost:8000/listar_filmes').then((res) => {
    return res.json();
}).then((data) => {

    //Deixar vazio
    lis.innerHTML = '';

    data.forEach((lista) => {

        //Confirmar item que vai ser listado
        if(typeof lista !== 'object' || lista === null || !lista.nome || !lista.id){
            return;
        }

        const filmeId = lista.id; 

        lis.innerHTML += `
        <li>
            <strong>Nome do Filme: </strong> ${lista.nome} </br>
            <strong>Atores: </strong> ${lista.atores} </br>
            <strong>Diretor: </strong> ${lista.diretor} </br>
            <strong>Ano de Lançamento: </strong> ${lista.ano_lancamento} </br>
            <strong>Genero: </strong> ${lista.genero} </br>
            <strong>Produtora: </strong> ${lista.produtora} </br>
            <strong>Sinopse: </strong> ${lista.sinopse} </br>
            <button onclick="irParaEdicao('${filmeId}')">Editar</button>
            
            <button onclick="deletarFilme('${filmeId}')">Excluir</button>
            <hr>
        </li>
        `
    });
});