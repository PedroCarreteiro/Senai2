from tamagoshi import Tamagoshi

class Urso(Tamagoshi):
    def __init__(self, nome, armadura):
        super().__init__(nome)
        self.armadura = armadura

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade/120)

    def brincar(self, quantidade):
        return super().brincar(quantidade)

    def getHumor(self):
        return super().getHumor()
    
    def vida(self):
        return super().vida()
    
    def tempoPassando(self):
        self.vida()
        self.idade += 0.1
        self.tedio += 5
        self.fome += 10

    def dormir(self):
        if self.vida < 100:
            self.vida += 20
            print(f"Vida regenerada em 10")
            if self.vida > 100:
                self.vida = self.vida - (self.vida-100)
        else:
            print("Já está com a vida máxima!")

    def treinar(self):
        if self.forca < 100:
            self.forca += 20
            self.fome += 20
            print(
                f"Força aumentou em 20\n"
                f"Fome aumentou em 20\n"
            )
            if self.forca > 100:
                self.forca = self.forca - (self.forca-100)
        else:
            print("Já está com a força máxima!")

    def estudar(self):
        if self.tedio > 0:
            self.tedio -= 10
            print(
                f"Tedio diminuiu em 20\n"
            )
            if self.tedio < 0:
                self.tedio = self.tedio + (self.tedio-100)
        else:
            print("Já está sem tedio!")