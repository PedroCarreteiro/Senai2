import random

from tamagoshi import Tamagoshi
from lobo import Lobo
from urso import Urso
from grifo import Grifo



def main():
    print(" ==== Bem vindo ao SUPER TAMAGOSHI 40000 ==== ")
    escolha = True
    while escolha == True:
        escolha_classe = input(f"Qual classe a classe do seu Tamagoshi: \n"
                                    f"[1] - Lobo\n"
                                    f"[2] - Urso\n"
                                    f"[3] - Grifo\n"
                                    f"[4] - Aleatória\n")
        
        

        if escolha_classe == "4":
            print("Você escolheu uma classe aleatória, logo aparecerá qual é a sua classe.")
            escolha_classe = str(random.randint(1,3))

        if escolha_classe == "1":
            print("Sua classe é LOBO")
            classe = Lobo
            escolha = False
        elif escolha_classe == "2":
            print("Sua classe é URSO")
            classe = Urso
            escolha = False
        elif escolha_classe == "3":
            print("Sua classe é GRIFO")
            classe = Grifo
            escolha = False
        else:
            print("Atenção! O digito não corresponde a nenhuma classe!")

    
    classe.nome = input("\n\nDigite o nome do seu Tamagoshi: ")
    print("O nome do seu Tamagoshi é: "+classe.nome)


    while True:
       if classe == Lobo:
           acao = input("\nDigite sua ação: ")





        


main()

    



