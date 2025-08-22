from tamagoshi import Tamagoshi

class Lobo(Tamagoshi):
    def __init__(self, nome, forca):
        super().__init__(nome)
        self.forca = forca
        
    def alimentar(self):
        return super().alimentar()

    def brincar(self):
        return super().brincar()

    def getHumor(self):
        return super().getHumor()
    
    def vida(self):
        return super().vida()
    
    def tempoPassando(self):
        return super().tempoPassando()
    
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

    def treinarForca(self):
        if self.forca < 100:
            self.forca += 10
            self.fome += 10
            print(
                f"Força aumentou!\n"
                f"Fome aumentou!\n"
            )
            if self.forca > 100:
                self.forca = 100
        else:
            print("Já está com a força máxima!\n")

    def utilizarIgni(self):
        if self.tedio > 0:
            self.tedio -= 10
            print(f"Tedio diminuiu!\n")
            if self.tedio < 0:
                self.tedio = 0
        else:
            print("Já está zero de tedio!\n")