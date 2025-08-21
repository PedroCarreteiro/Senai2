class Tamagoshi():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    # def alimentar(self, quantidade):
    #     if (quantidade >= 0) and (quantidade <= 100):
    #         self.fome -= self.fome * (quantidade/100)

    # def brincar(self, quantidade):
    #     if (quantidade >= 0) and (quantidade <= 100):
    #         self.tedio -= self.tedio * (quantidade/100)


    def alimentar(self):
        if self.fome > 0:
            self.fome -= 5
            print(f"Fome diminuiu em 5")
            if self.fome < 0:
                self.fome = 0
        else:
            print("Já está zero de fome")

    def brincar(self):
        if self.tedio > 0:
            self.tedio -= 5
            print(f"Tedio diminuiu em 5")
            if self.tedio < 0:
                self.tedio = 0
        else:
            print("Já está zero de tedio")

    def getHumor(self):
        print(f"O humor do(a) {self.nome} é -",((self.fome + self.tedio)/2))
        return ((self.fome + self.tedio)/2)
        
    
    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <= 60):
            self.saude -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <= 80):
            self.saude -= 30
        elif (self.fome > 80 and self.fome <= 90) or (self.tedio > 80 and self.tedio <= 90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            print("!Estoy a morer!")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("!Su Tamagoshi está muerto T_T!")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 1
        self.fome += 2

    #novo
    def getStatus(self):
        print(f"Saude: {self.saude}\n"
              f"Idade: {self.idade}\n"
              f"Tedio: {self.tedio}\n"
              f"Fome: {self.fome}\n")
        
