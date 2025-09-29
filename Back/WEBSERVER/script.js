const lis = document.querySelector('#idlistinea')

// -----------------------------------------------------------
// FUNÇÃO AUXILIAR: Redireciona para a página de edição
// -----------------------------------------------------------
// Esta função simula o "link" para a página de edição,
// passando o ID via URL (Ex: editar.html?id=123)
function irParaEdicao(id) {
    // Redireciona para a página de edição, passando o ID do filme na query string
    window.location.href = `editar.html?id=${id}`;
}


// =========================================================================
// LÓGICA EXCLUSIVA PARA A PÁGINA DE EDIÇÃO (editar.html)
// =========================================================================

// Função auxiliar para obter parâmetros da URL (Ex: ?id=123)
function getFilmeIdFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

// Função que carrega o filme e preenche o formulário
async function carregarDadosParaEdicao() {
    const filmeId = getFilmeIdFromUrl();
    const form = document.getElementById('form-edicao');

    if (!form || !filmeId) {
        // Não estamos na página de edição ou o ID está faltando
        return; 
    }

    // 1. Fazer GET para obter todos os filmes e encontrar o filme específico
    try {
        const response = await fetch('http://localhost:8000/listar_filmes');
        if (!response.ok) throw new Error('Falha ao carregar a lista de filmes.');
        
        const filmes = await response.json();
        const filme = filmes.find(f => String(f.id) === filmeId); // Compara como string

        if (!filme) {
            alert("Filme não encontrado!");
            window.location.href = 'listar_filmes.html';
            return;
        }

        // 2. Preencher os campos do formulário com os dados atuais
        document.getElementById('filme-nome-atual').textContent = filme.nome; // Atualiza o título
        document.getElementById('filme-id').value = filmeId; // Campo oculto
        
        document.getElementById('nome_filme').value = filme.nome || '';
        document.getElementById('atores').value = filme.atores || '';
        document.getElementById('diretor').value = filme.diretor || '';
        document.getElementById('ano_lancamento').value = filme.ano_lancamento || '';
        document.getElementById('genero').value = filme.genero || '';
        document.getElementById('produtora').value = filme.produtora || '';
        document.getElementById('sinopse').value = filme.sinopse || '';

        // 3. Configurar o evento de submissão do formulário
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Coletar todos os dados do formulário
            const formData = new FormData(e.target);
            const dadosPatch = {};
            
            // Criar o objeto JSON a ser enviado
            for (const [key, value] of formData.entries()) {
                // Não incluir o campo oculto 'filme-id' no PATCH body
                if (key !== 'filme-id') { 
                    dadosPatch[key] = value.trim();
                }
            }

            // Chamar a função de envio do PATCH
            enviarPatch(filmeId, dadosPatch);
        });

    } catch (error) {
        console.error("Erro ao carregar dados de edição:", error);
        alert("Não foi possível carregar os dados para edição.");
        window.location.href = 'listar_filmes.html';
    }
}

// Executa a função de carregamento assim que a página estiver pronta
document.addEventListener('DOMContentLoaded', carregarDadosParaEdicao);


// =========================================================================
// FUNÇÃO DE ENVIO DO PATCH (enviada por você em uma resposta anterior, adaptada)
// =========================================================================
// OBS: Esta função precisa estar definida no seu script.js.
function enviarPatch(id, dadosPatch) {
    
    fetch(`http://localhost:8000/filmes_mari/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(dadosPatch)
    })
    .then(response => {
        if (response.ok) {
            alert(`Filme ID ${id} atualizado com sucesso!`);
            
            // REDIRECIONAMENTO APÓS SUCESSO DO PATCH
            window.location.href = 'listar_filmes.html'; 
            
        } else {
            alert('Erro ao tentar atualizar o filme. Verifique o servidor.');
        }
    })
    .catch(error => {
        console.error('Erro na requisição PATCH:', error);
        alert('Erro de conexão ao tentar atualizar.');
    });
}


// -----------------------------------------------------------
// FUNÇÃO DELETE (Exclusão): Faz o refresh
// -----------------------------------------------------------
function deletarFilme(id) {
    if (!confirm(`Tem certeza que deseja excluir o filme com ID ${id}?`)) {
        return;
    }

    fetch(`http://localhost:8000/filmes_mari/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            alert(`Filme ${id} excluído com sucesso!`);
            
            // <<< MANTÉM NA PÁGINA, APENAS RECARREGA A LISTA (refresh)
            window.location.reload(); 
            
        } else {
            alert('Erro ao tentar excluir o filme.');
        }
    })
    .catch(error => {
        console.error('Erro na requisição DELETE:', error);
        alert('Erro de conexão ao tentar excluir.');
    });
}


// -----------------------------------------------------------
// CARREGAMENTO E RENDERIZAÇÃO INICIAL DA LISTA
// -----------------------------------------------------------
fetch('http://localhost:8000/listar_filmes').then((res) => {
    return res.json();
}).then((data) => {
    data.map((lista) => {
        const filmeId = lista.id; 

        lis.innerHTML += `
        <li>
            <strong>Nome do Filme: <strong/> ${lista.nome} </br>
            <strong>Atores: <strong/> ${lista.atores} </br>
            <strong>Diretor: <strong/> ${lista.diretor} </br>
            <strong>Ano de Lançamento: <strong/> ${lista.ano_lancamento} </br>
            <strong>Genero: <strong/> ${lista.genero} </br>
            <strong>Produtora: <strong/> ${lista.produtora} </br>
            <strong>Sinopse: <strong/> ${lista.sinopse} </br>
            <button onclick="irParaEdicao('${filmeId}')">Editar</button>
            
            <button onclick="deletarFilme('${filmeId}')">Excluir</button>
            <hr>
        <li/>
        `
    })
})