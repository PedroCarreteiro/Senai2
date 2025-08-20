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
            print(f"Vida regenerada em 20")
            if self.vida > 100:
                self.vida = self.vida - (self.vida-100)
        else:
            print("Já está com a vida máxima!")

    def treinarArmadura(self):
        if self.armadura < 100:
            self.armadura += 20
            self.fome += 20
            print(
                f"Armadura aumentou em 20\n"
                f"Fome aumentou em 20\n"
            )
            if self.armadura > 100:
                self.armadura = self.armadura - (self.armadura-100)
        else:
            print("Já está com a armadura máxima!")

    def utilizarQuen(self):
        if self.armadura < 100:
            self.armadura += 5
            print(
                f"Armadura aumentou em 5\n"
            )
            if self.armadura > 100:
                self.armadura = self.armadura - (self.armadura-100)
        else:
            print("Já está com a armadura máxima!")