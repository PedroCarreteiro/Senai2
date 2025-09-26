#Importar bibliotecas
import json
from logging import Handler
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json


filmes = {}

id_counter = 0


#Classe para o servidor
class MyHandle(SimpleHTTPRequestHandler):
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
        #Caso o caminho seja o de login, o bloco abaixo será executado e caso ocorra um erro, a exceção será chamada
        if self.path == "/login":
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
        elif self.path == "/cadastro":
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


        #Caso o caminho seja o de listar filmes, o bloco abaixo será executado e caso ocorra um erro, a exceção será chamada
        elif self.path == "/listar_filmes":
            #Bloco de código para abrir o arquivo listar_filmes.html e colocar seu conteúdo na var content
            try:
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), encoding='utf-8') as listar_filmes:
                    content = listar_filmes.read()

                #Variável para armazenar o conteúdo html do filme
                filmes_html = ""

                #Se não tiver nenhum filme, uma mensagem de nenhum filme cadastrado aparecerá
                if not filmes:
                    filmes_html = '<p>Nenhum filme cadastrado</p>'
                #Caso tenha algum filme, criará o html do filme
                else:
                    for filme_id, filme_data in filmes.items():
                        filmes_html += f"""
                        <article>
                            <h3>{filme_data.get('nome')}</h3>
                            <p><strong>Atores:</strong> {filme_data.get('atores')}</p>
                            <p><strong>Diretor:</strong> {filme_data.get('diretor')}</p>
                            <p><strong>Ano:</strong> {filme_data.get('ano_lancamento',)}</p>
                            <p><strong>Genero:</strong> {filme_data.get('genero')}</p>
                            <p><strong>Produtora:</strong> {filme_data.get('produtora')}</p>
                            <p><strong>Sinopse:</strong> {filme_data.get('sinopse')}</p>
                            <br>
                        </article>
                        """

                #Dar replace no comentário do html pelo conteúdo do filme
                final_content = content.replace('<!--FILMES-->',filmes_html)

                #Enviar resposta de sucesso e dados do header
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                #Escrever o conteúdo guardado no content na tela com a encodificação utf-8
                self.wfile.write(final_content.encode('utf-8'))
            #Exceção que envia um erro 404 caso o try não funcione corretamente
            except FileNotFoundError:
                self.send_error(404, "File Not Found")


        #Caso o caminho seja o de listar filmes, o bloco abaixo será executado e caso ocorra um erro, a exceção será chamada
        elif self.path == "/listar_filmes_mari":
            arquivo = "dados.json"

            if os.path.exists(arquivo):
                with open(arquivo, encoding='utf-8') as listagem:
                    try:
                        filmes_mari = json.load(listagem)
                    except json.JSONDecodeError:
                        filmes_mari = []

            else:
                filmes_mari = []

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filmes_mari).encode("utf-8"))

        #Caso nenhum caminho tenha sido especificado, a superclasse será executada
        else:
            super().do_GET()

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
            
            #Criar o dicionário do filme
            filme_mari = {
                "nome": nome_filme,
                "atores": atores,
                "diretor": diretor,
                "ano_lancamento": ano_lancamento,
                "genero": genero,
                "produtora": produtora,
                "sinopse": sinopse
            }

            arquivo = "dados.json"

            if os.path.exists(arquivo):
                with open(arquivo, encoding="utf-8") as lista:
                    try:
                        filmes_mari = json.load(lista)
                    except json.JSONDecodeError:
                        filmes_mari = []
                filmes_mari.append(filme_mari)
            else:
                filmes_mari = [filme_mari]


            #Transformar a lista em json
            with open(arquivo, "w", encoding="utf-8") as lista:
                json.dump(filmes_mari, lista, indent=4, ensure_ascii=False)
            
            
            # Enviar resposta de sucesso
            self.send_response(201) # 201 Created
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(filme_mari).encode("utf-8"))

        #Padrão que sempre tem
        else:
            super().do_POST()


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

