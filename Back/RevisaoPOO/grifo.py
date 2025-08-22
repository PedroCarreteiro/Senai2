from tamagoshi import Tamagoshi

class Grifo(Tamagoshi):
    def __init__(self, nome, inteligencia):
        super().__init__(nome)
        self.inteligencia = inteligencia

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
        self.idade += 0.01
        self.tedio += 1
        self.fome += 2

    def getStatus(self):
        return super().getStatus()

    def beberPocao(self):
        if self.saude < 100:
            self.saude += 10
            print(f"Saude regenerada!\n")
            if self.saude > 100:
                self.saude = 100
        else:
            print("Já está com a saude máxima!\n")

    def estudar(self):
        if self.inteligencia < 100:
            self.inteligencia += 20
            print(
                f"Inteligência aumentou!\n"
            )
            if self.inteligencia > 100:
                self.inteligencia = 100
        else:
            print("Já está com a inteligência máxima!\n")

    def utilizarAxii(self):
        if self.tedio > 0:
            self.tedio -= 10
            print(
                f"Tedio diminuiu!\n"
            )
            if self.tedio < 0:
                self.tedio = 0
        else:
            print("Já está sem tedio!\n")