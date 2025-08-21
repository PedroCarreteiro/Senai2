from tamagoshi import Tamagoshi

class Urso(Tamagoshi):
    def __init__(self, nome, armadura):
        super().__init__(nome)
        self.armadura = armadura

    def alimentar(self):
        return super().alimentar()
        
    def brincar(self):
        return super().brincar()

    def getHumor(self):
        return super().getHumor()
    
    def vida(self):
        return super().vida()
    
    def tempoPassando(self):
        self.vida()
        self.idade += 0.1
        self.tedio += 2
        self.fome += 3

    def getStatus(self):
        return super().getStatus()

    def dormir(self):
        if self.saude < 100:
            self.saude += 20
            print(f"saude regenerada em 20")
            if self.saude > 100:
                self.saude = 100
        else:
            print("Já está com a saude máxima!")

    def treinarArmadura(self):
        if self.armadura < 100:
            self.armadura += 20
            self.fome += 20
            print(
                f"Armadura aumentou em 20\n"
                f"Fome aumentou em 20\n"
            )
            if self.armadura > 100:
                self.armadura = 100
        else:
            print("Já está com a armadura máxima!")

    def utilizarQuen(self):
        if self.armadura < 100:
            self.armadura += 5
            print(
                f"Armadura aumentou em 5\n"
            )
            if self.armadura > 100:
                self.armadura = 100
        else:
            print("Já está com a armadura máxima!")