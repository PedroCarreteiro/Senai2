class Veiculo:
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.qnt_porta = qnt_porta
        self.modelo = modelo

    def andar(self):
        print(f"{self.modelo} andando")

    def parar(self):
        print(f"{self.moelo} parado")

    def imprimir(self):
        print(
            "O veículo tem as características: \n"
            f"Marca: {self.marca}\n"
            f"Ano de fabricação: {self.ano_fab}\n"
            f"Cor: {self.cor}\n"
            f"Tem {self.qnt_porta} porta(s)\n"
        )

def main():
    carro1 = Veiculo("Honda", 2008, "Azul", 4, "Civic")
    carro1.imprimir()

main()

class Carro(Veiculo):
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo, litragem, carroceria):
        super().__init__(marca, ano_fab, cor, qnt_porta, modelo)
        self.litragem = litragem
        self.carroceria = carroceria

    def chamarNaSeta(self):
        print(f"{self.modelo} está chamando na seta!")

    def darPipoco(self):
        print(f"Um motor de {self.litragem} litros está dando uns pipoco!")

    def imprimir(self):
        print(
            "O veículo tem as características: \n"
            f"Marca: {self.marca}\n"
            f"Ano de fabricação: {self.ano_fab}\n"
            f"Cor: {self.cor}\n"
            f"Tem {self.qnt_porta} porta(s)\n"
            f"Litragem: {self.litragem}\n"
            f"Carroceria: {self.carroceria}\n"
        )

class Moto(Veiculo):
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo, cilindradas):
        super().__init__(marca, ano_fab, cor, qnt_porta, modelo)
        self.cilindradas = cilindradas
    
    def darGrau(self):
        print(f"{self.modelo} está dando grau!")

    def imprimir(self):
        print(
            "O veículo tem as características: \n"
            f"Marca: {self.marca}\n"
            f"Ano de fabricação: {self.ano_fab}\n"
            f"Cor: {self.cor}\n"
            f"Tem {self.qnt_porta} porta(s)\n"
            f"Cilindradas: {self.cilindradas}\n"
        )

class Caminhao(Veiculo):
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo, qtd_eixos):
        super().__init__(marca, ano_fab, cor, qnt_porta, modelo)
        self.qtd_eixos = qtd_eixos

    def quebraDeAsa(self):
        print(f"{self.modelo} está fazendo uma quebra de asa")
    
    def imprimir(self):
        print(
            "O veículo tem as características: \n"
            f"Marca: {self.marca}\n"
            f"Ano de fabricação: {self.ano_fab}\n"
            f"Cor: {self.cor}\n"
            f"Tem {self.qnt_porta} porta(s)\n"
            f"Qtd eixos: {self.qtd_eixos}\n"
        )

carro = Carro("Nissan", 1999, "Azul", 2, "GTR", 4, "Sedan")
carro.imprimir()
carro.chamarNaSeta()
carro.darPipoco()
print(f"\n\n")

moto = Moto("Yamaha", 2010, "Branco", 0, "XJ6", 600)
moto.imprimir()
moto.darGrau()
print(f"\n\n")

caminhao = Caminhao("Mercedes", 1999, "Amarelo", 2, "1113", 3)
caminhao.imprimir()
caminhao.quebraDeAsa()
print(f"\n\n")
        


