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

import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandle(SimpleHTTPRequestHandler):
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
    
    def do_GET(self):
        if self.path == "/login":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>LOGIN DA FESTA DO CARLINHOS MAIA</h1></body></html>")
        else:
            super().do_GET()

def main():
    server_address = ('',8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server Running in http://localhost:8000")
    httpd.serve_forever()

main()

