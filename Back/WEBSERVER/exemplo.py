# from http.server import SimpleHTTPRequestHandler, HTTPServer

# #Definir a porta
# port = 8000

# #Definindo o gerenciamento/manipulador de requisições
# handler = SimpleHTTPRequestHandler

# #Criação de instancia de servidor
# server = HTTPServer(("localhost",port), handler)

# #imprimindo mensagem de ok
# print(f"Server Runing in localhost:{port}")

# server.serve_forever()

#Importar bibliotecas
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

#Classe para o servidor
class MyHandle(SimpleHTTPRequestHandler):
    #Função para listar os caminhos do servidor, e abrindo o index.html por padrão
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), 'r')

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #Especificando a codificação como utf-8
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
    
    #Função para realizar as operações do método GET a depender do caminho especificado
    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), "login.html"), 'r') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                #self.wfile.write(b"<html><body><h1>LOGIN DA FESTA DO CARLINHOS MAIA</h1></body></html>")
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")


        elif self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), 'r') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")


        elif self.path == "/listar_filmes":
            try:
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), 'r') as listar_filmes:
                    content = listar_filmes.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        else:
            super().do_GET()



def main():
    server_address = ('',8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server Running in http://localhost:8000")
    httpd.serve_forever()

main()

