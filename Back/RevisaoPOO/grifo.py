from tamagoshi import Tamagoshi

class Grifo(Tamagoshi):
    def __init__(self, nome, inteligencia):
        super().__init__(nome)
        self.inteligencia = inteligencia

    def alimentar(self, quantidade):
        return super().alimentar(quantidade)

    def brincar(self, quantidade):
        return super().brincar(quantidade)

    def getHumor(self):
        return super().getHumor()
    
    def vida(self):
        return super().vida()
    
    def tempoPassando(self):
        self.vida()
        self.idade += 0.01
        self.tedio += 3
        self.fome += 5

    def beberPocao(self):
        if self.vida < 100:
            self.vida += 10
            print(f"Vida regenerada em 10")
            if self.vida > 100:
                self.vida = self.vida - (self.vida-100)
        else:
            print("Já está com a vida máxima!")

    def estudar(self):
        if self.inteligencia < 100:
            self.inteligencia += 20
            print(
                f"Inteligência aumentou em 20\n"
            )
            if self.inteligencia > 100:
                self.inteligencia = self.inteligencia - (self.inteligencia-100)
        else:
            print("Já está com a inteligência máxima!")

    def utilizarAxii(self):
        if self.tedio > 0:
            self.tedio -= 10
            print(
                f"Tedio diminuiu em 10\n"
            )
            if self.tedio < 0:
                self.tedio = self.tedio + (self.tedio-100)
        else:
            print("Já está sem tedio!")