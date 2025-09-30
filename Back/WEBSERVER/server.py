#Importar bibliotecas
import json
from logging import Handler
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json


filmes = {}

id_counter = 0

#Arquivo de dados
ARQUIVO_DADOS = "dados.json"


#Classe para o servidor
class MyHandle(BaseHTTPRequestHandler):
    
    #Carregar filmes do arquivo dados.json
    def carregar_filmes(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, encoding='utf-8') as lista:
                    return json.load(lista)
            except json.JSONDecodeError:
                return []
        return []

    #Salvar os dados no arquivo dados.json
    def salvar_filme(self, filmes_list):
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as lista:
            json.dump(filmes_list, lista, indent=4, ensure_ascii=False)
    
    #Função para listar os caminhos do servidor
    def list_directory(self, path):
        #Tentar executar o código abaixo, e caso ocorra um erro, a exceção é chamada
        try:
            #Abrir o arquivo index.html
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')
            #Enviar uma resposta de sucesso e definir dados do header
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #Especificando a codificação do arquivo como utf-8 e escrever o conteúdo na tela
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            #Retornar None para sinalizar que já utilizamos tudo o que precisávamos
            return None
        #Caso ocorra algum erro, é chamada a exceção e ela passa para a próxima etapa
        except FileNotFoundError:
            pass
        #Retornar o original não de certo o try para abrir o index, ele retorna os caminhos
        return super().list_directory(path)
    

    #Função para realizar a verificação de login, onde apenas identificará o user se o conteúdo dos campos estiver igual ao das vars
    def account_user(self, login, password):

        loga = "pedro@email.com"
        senha = "123456"

        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe"
            

    #Função para realizar as operações do método GET a depender do caminho especificado
    def do_GET(self):
        #Pegar a URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        #Caso o caminho seja o de login, o bloco abaixo será executado e caso ocorra um erro, a exceção será chamada
        if path == "/login":
            #Bloco de código para abrir o arquivo login.html e colocar seu conteúdo na var content
            try:
                with open(os.path.join(os.getcwd(), "login.html"), encoding='utf-8') as login:
                    content = login.read()
                #Enviar resposta de sucesso e dados do header 
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                #Escrever o conteúdo guardado no content na tela com a encodificação utf-8
                self.wfile.write(content.encode('utf-8'))
            #Exceção que envia um erro 404 caso o try não funcione corretamente
            except FileNotFoundError:
                self.send_error(404, "File Not Found")


        #Caso o caminho seja o de cadastro, o bloco abaixo será executado e caso ocorra um erro, a exceção será chamada
        elif path == "/cadastro":
            #Bloco de código para abrir o arquivo cadastro.html e colocar seu conteúdo na var content
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                #Enviar resposta de sucesso e dados do header 
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                #Escrever o conteúdo guardado no content na tela com a encodificação utf-8
                self.wfile.write(content.encode('utf-8'))
            #Exceção que envia um erro 404 caso o try não funcione corretamente
            except FileNotFoundError:
                self.send_error(404, "File Not Found")


       #Retornar a lista de jsons
        elif path == "/listar_filmes":
            # Carregar filmes
            filmes_mari = self.carregar_filmes()

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filmes_mari).encode("utf-8"))
            return # Importante: Adicionar 'return'

        #Carregar a página que lista os filmes em html
        elif path == "/listar_filmes_html":
            try:
                # Carrega o arquivo HTML puro
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), encoding='utf-8') as f:
                    content = f.read()
                
                #Enviar resposta de sucesso e dados do header 
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                #Escrever o conteúdo guardado no content na tela com a encodificação utf-8
                self.wfile.write(content.encode('utf-8'))
                return
                
            #Caso não encontre o arquivo
            except FileNotFoundError:
                self.send_error(404, "Arquivo HTML de listagem (listar_filmes.html) não encontrado")
                return

        #Caso nenhum caminho tenha sido especificado
        else:
            #Se for a raiz, mostrar index.html
            if path == '/':
                return self.list_directory(os.getcwd())

            #Se for um caminho para um arquivo estático
            try:
                #Remover a barra inicial e abrir o arquivo
                file_path = path[1:]
                
                #Mostrar o arquivo
                if os.path.exists(file_path) and not os.path.isdir(file_path):
                    
                    #Tipo do arquivo
                    mime_type = 'application/octet-stream'
                    if file_path.endswith('.html'):
                        mime_type = 'text/html'
                    elif file_path.endswith('.css'):
                        mime_type = 'text/css'
                    elif file_path.endswith('.js'):
                        mime_type = 'application/javascript'
                    
                    #Abrir aarquivo
                    with open(file_path, 'rb') as f:
                        self.send_response(200)
                        self.send_header("Content-type", mime_type)
                        self.end_headers()
                        self.wfile.write(f.read())
                        return

            except Exception:
                pass
                
            #Se não for a raiz e não for um arquivo encontrado
            self.send_error(404, "Caminho ou arquivo não mapeado")

    #Requisições POST
    def do_POST(self):
        if self.path == '/send_login':
            #O que veio do post do form
            #Ver o tamanho
            content_length = int(self.headers['Content-length'])
            #Ler o que veio
            body = self.rfile.read(content_length).decode('utf-8')
            #Pegar as informações do que veio
            form_data = parse_qs(body)

            #Armazenar o conteúdo dos inputs em vars
            login = form_data.get('nome_usuario',[""])[0]
            password = form_data.get('senha',[""])[0]

            #Tratamento de espaços sobressalents
            login = login.strip()
            password = password.strip()

            #Verificar se o usuario logou ou não através da função
            logou = self.account_user(login, password)
    
            #Printar os dados dos inputs
            print("Data Form:")
            print("Usuario: ", form_data.get('nome_usuario', [""])[0]) 
            print("Password: ", form_data.get('senha', [""])[0]) 
    
            #Retornar sucesso
            self.send_response(200)
            #Retornar o header
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #Mensagem de sucesso (pode ser uma nova página)
            self.wfile.write(logou.encode("utf-8"))

        #Pegar o caminho que está no formulário de cadastro no html para cadastrar um filme
        elif self.path == '/send_filme':
            #Contador para os ids
            global id_counter
            
            #Ler o tamanho do corpo da requisição
            content_length = int(self.headers['Content-length'])
            #Ler o que veio
            body = self.rfile.read(content_length).decode('utf-8')
            #Pegar as informações do que veio
            form_data = parse_qs(body)

            #Extrair os dados do formulário
            nome_filme = form_data.get('nome_filme', [""])[0].strip()
            atores = form_data.get('atores', [""])[0].strip()
            diretor = form_data.get('diretor', [""])[0].strip()
            ano_lancamento = form_data.get('ano_lancamento', [""])[0].strip()
            genero = form_data.get('genero', [""])[0].strip()
            produtora = form_data.get('produtora', [""])[0].strip()
            sinopse = form_data.get('sinopse', [""])[0].strip()
            
            #Aumentar o contador
            id_counter += 1
            #Transferir o contador para str
            filme_id = str(id_counter)
            
            #Criar o dicionário do filme
            filme = {
                "nome": nome_filme,
                "atores": atores,
                "diretor": diretor,
                "ano_lancamento": ano_lancamento,
                "genero": genero,
                "produtora": produtora,
                "sinopse": sinopse
            }

            #Adicionar o filme ao dicionário de filmes
            filmes[filme_id] = filme
            
            #Resposta JSON
            response = {
                "message": "Filme cadastrado com sucesso!",
                "filme_id": filme_id,
                "filme": filme
            }
            
            # Enviar resposta de sucesso
            self.send_response(201) # 201 Created
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))


        elif self.path == '/send_filme_mari':
            
            #Ler o tamanho do corpo da requisição
            content_length = int(self.headers['Content-length'])
            #Ler o que veio
            body = self.rfile.read(content_length).decode('utf-8')
            #Pegar as informações do que veio
            form_data = parse_qs(body)

            #Extrair os dados do formulário
            nome_filme = form_data.get('nome_filme', [""])[0].strip()
            atores = form_data.get('atores', [""])[0].strip()
            diretor = form_data.get('diretor', [""])[0].strip()
            ano_lancamento = form_data.get('ano_lancamento', [""])[0].strip()
            genero = form_data.get('genero', [""])[0].strip()
            produtora = form_data.get('produtora', [""])[0].strip()
            sinopse = form_data.get('sinopse', [""])[0].strip()
            
            #Puxar os dados dos jsons
            filmes_mari = self.carregar_filmes()
            
            #Novo id único
            max_id = max([f.get('id', 0) for f in filmes_mari]) if filmes_mari else 0
            new_id = max_id + 1

            #Criar o dicionário do filme
            filme_mari = {
                "id": new_id,
                "nome": nome_filme,
                "atores": atores,
                "diretor": diretor,
                "ano_lancamento": ano_lancamento,
                "genero": genero,
                "produtora": produtora,
                "sinopse": sinopse
            }

            filmes_mari.append(filme_mari)
            
            #Transformar a lista em json
            self.salvar_filme(filmes_mari)
            
            #Enviar resposta de sucesso
            self.send_response(201) # 201 Created
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filme_mari).encode("utf-8"))

        #Padrão que sempre tem
        else:
            super().do_POST()

    #Patch
    def do_PATCH(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.split('/')
        
        #Pegar a URL
        if len(path_parts) == 3 and path_parts[1] == 'filmes_mari':
            try:
                filme_id = int(path_parts[2])
            except ValueError:
                self.send_error(400, "ID do filme inválido.")
                return

            #Carregar os filmes
            filmes_mari = self.carregar_filmes()
            
            #Encontrar o filme
            filme_encontrado = None
            filme_index = -1
            for i, filme in enumerate(filmes_mari):
                if filme.get('id') == filme_id:
                    filme_encontrado = filme
                    filme_index = i
                    break
            
            #Caso o filme não seja encontrado
            if filme_encontrado is None:
                self.send_error(404, "Filme não encontrado.")
                return
            
            #Corpo da requisição
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                try:
                    body = self.rfile.read(content_length)
                    dados_patch = json.loads(body.decode('utf-8'))
                except json.JSONDecodeError:
                    self.send_error(400, "JSON Inválido no corpo da requisição.")
                    return
                
                # Aplica as atualizações parciais
                for chave, valor in dados_patch.items():
                    if chave in filme_encontrado and chave != 'id': 
                        filme_encontrado[chave] = valor
                
                #Salvar os dados e enviar
                filmes_mari[filme_index] = filme_encontrado
                self.salvar_filme(filmes_mari)

                self.send_response(200) # 200 OK
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(filme_encontrado).encode("utf-8"))
            else:
                self.send_error(400, "Corpo da requisição vazio.")
        else:
            self.send_error(404, "Caminho PATCH inválido. Use /filmes_mari/<ID>")


    #Delete
    def do_DELETE(self):

        #Pegar a URL
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.split('/')
        
        if len(path_parts) == 3 and path_parts[1] == 'filmes_mari':
            try:
                filme_id = int(path_parts[2])
            except ValueError:
                self.send_error(400, "ID do filme inválido.")
                return

            #Carregar os filmes
            filmes_mari = self.carregar_filmes()
            
            filme_index_to_delete = -1
            for i, filme in enumerate(filmes_mari):
                if filme.get('id') == filme_id:
                    filme_index_to_delete = i
                    break
            
            if filme_index_to_delete == -1:
                self.send_error(404, "Filme não encontrado.")
                return

            # Remove o filme e salva
            filmes_mari.pop(filme_index_to_delete)
            self.salvar_filme(filmes_mari)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": f"Filme com ID {filme_id} removido com sucesso."}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_error(404, "Caminho DELETE inválido. Use /filmes_mari/<ID>")


#Função main para iniciar o servidor
def main():
    #Iniciar o servidor na porta 8000
    server_address = ('',8000)
    #Objeto para indicar o endereço do server e que ele será utilizado com o MyHandle
    httpd = HTTPServer(server_address, MyHandle)
    #Imprimir o caminho do servidor
    print("Server Running in http://localhost:8000")
    #Ficar com o servidor iniciado indefinidamente
    httpd.serve_forever()

#Chamar a função main
main()