#Importar bibliotecas
from logging import Handler
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


filmes = {}


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
    

    def account_user(self, login, password):

        loga = "pedro@email.com"
        senha = "123456"

        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe"
        
    def cadastrar_filme(self, nome_filme, atores, diretor, ano_lancamento, genero, produtora, sinopse):
        try:
            filme = {
                "nome": nome_filme,
                "atores": atores,
                "diretor": diretor,
                "ano_lancamento": ano_lancamento,
                "genero": genero,
                "produtora": produtora,
                "sinopese": sinopse
            }
            filmes["filme"] = filme
            return filmes
        except:
            return "Erro"
            

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
                #Enviar resposta de sucesso e dados do header
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                #Escrever o conteúdo guardado no content na tela com a encodificação utf-8
                self.wfile.write(content.encode('utf-8'))
            #Exceção que envia um erro 404 caso o try não funcione corretamente
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        #Caso nenhum caminho tenha sido especificado, a superclasse será executada
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/send_login':
            #O que veio do post do form
            #Ver o tamanho
            content_length = int(self.headers['Content-length'])
            #Ler o que veio
            body = self.rfile.read(content_length).decode('utf-8')
            #Pegar as informações do que veio
            form_data = parse_qs(body)

            login = form_data.get('nome_usuario',[""])[0]
            password = form_data.get('senha',[""])[0]

            login = login.strip()
            password = password.strip()

            logou = self.account_user(login, password)
 
            print("Data Form:")
            #Pegar os dados dos inputs
            print("Usuario: ", form_data.get('nome_usuario', [""])[0])        
            print("Password: ", form_data.get('senha', [""])[0])    
 
            #Retornar sucesso
            self.send_response(200)
            #Retornar o header
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #Mensagem de sucesso (pode ser uma nova página)
            self.wfile.write(logou.encode("utf-8"))

        elif self.path == '/send_filme':
            content_length = int(self.headers['Content-length'])
            #Ler o que veio
            body = self.rfile.read(content_length).decode('utf-8')
            #Pegar as informações do que veio
            form_data = parse_qs(body)

            nome_filme = form_data.get('nome_filme',[""])[0]
            atores = form_data.get('atores',[""])[0]
            diretor = form_data.get('diretor',[""])[0]
            ano_lancamento = form_data.get('ano_lancamento',[""])[0]
            genero = form_data.get('genero',[""])[0]
            produtora = form_data.get('produtora',[""])[0]
            sinopse = form_data.get('sinopse',[""])[0]

            nome_filme = nome_filme.strip()
            atores = atores.strip()
            diretor = diretor.strip()
            ano_lancamento = ano_lancamento.strip()
            genero = genero.strip()
            produtora = produtora.strip()
            sinopse = sinopse.strip()
            
            cadastrar_filme = self.cadastrar_filme(nome_filme,atores,diretor,ano_lancamento,genero,produtora,sinopse)
 
            #Retornar sucesso
            self.send_response(200)
            #Retornar o header
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #Mensagem de sucesso (pode ser uma nova página)
            self.wfile.write(cadastrar_filme)

        #Padrão que sempre tem
        else:
            super(Handler, self).do_POST() 


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

