import random

from tamagoshi import Tamagoshi
from lobo import Lobo
from urso import Urso
from grifo import Grifo
import time

def passarTempo():
    print("\nCarregando...\n")
    time.sleep(3)

passarTempo()


def main():
    print(" ==== Bem vindo ao SUPER TAMAGOSHI 40000 ==== ")
    passarTempo()
    escolha = True
    while escolha == True:
        escolha_classe = input(f"Qual classe a classe do seu Tamagoshi: \n"
                                    f"[1] - Lobo\n"
                                    f"[2] - Urso\n"
                                    f"[3] - Grifo\n"
                                    f"[4] - Aleatória\n"
                                    f"[5] - Sair\n"
                                )


        if escolha_classe == "4":
            print("Você escolheu uma classe aleatória, logo aparecerá qual é a sua classe.")
            escolha_classe = str(random.randint(1,3))
            passarTempo()

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
        elif escolha_classe == "5":
            print("Você saiu do jogo!")
            escolha = False
        else:
            print("Atenção! O digito não corresponde a nenhuma classe!")

    passarTempo()
    if escolha_classe != "5":
        tamagoshi_nome = input("\n\nDigite o nome do seu Tamagoshi: ")
        tamagoshi = classe(tamagoshi_nome, 0)
        print(f"O nome do seu tamagoshi é: {tamagoshi.nome}")

        passarTempo()
        while True:

            if classe == Lobo:
                    
                    tamagoshi.tempoPassando()

                    acao = input(f"\nDigite sua ação: \n"
                                    f"[1] - Alimentar\n" 
                                    f"[2] - Brincar\n" 
                                    f"[3] - Beber Poção\n"
                                    f"[4] - Treinar Força\n"
                                    f"[5] - Utilizar Igni\n"
                                    f"[6] - Sair\n"
                                )
                    
                    passarTempo()

                    if acao == "1":
                        tamagoshi.alimentar()

                    elif acao == "2":
                        tamagoshi.brincar()

                    elif acao == "3":
                        tamagoshi.beberPocao()
                    
                    elif acao == "4":
                        tamagoshi.treinarForca()
                    
                    elif acao == "5":
                        tamagoshi.utilizarIgni()

                    elif acao == "6":
                        print("Você saiu do programa!")
                        break

                    tamagoshi.getStatus()

                    tamagoshi.getHumor()           
            
            
            elif classe == Urso:
                
                tamagoshi.tempoPassando()

                acao = input(f"\nDigite sua ação: \n"
                                    f"[1] - Alimentar\n" 
                                    f"[2] - Brincar\n" 
                                    f"[3] - Dormir\n"
                                    f"[4] - Treinar Armadura\n"
                                    f"[5] - Utilizar Quen\n"
                                    f"[6] - Sair\n"
                                )
                
                passarTempo()

                if acao == "1":
                        tamagoshi.alimentar()

                elif acao == "2":
                        tamagoshi.brincar()

                elif acao == "3":
                        tamagoshi.dormir()
                    
                elif acao == "4":
                        tamagoshi.treinarArmadura()
                    
                elif acao == "5":
                        tamagoshi.utilizarQuen()

                elif acao == "6":
                        print("Você saiu do programa!")
                        break
                
                tamagoshi.getStatus()

                tamagoshi.getHumor()
                
                

            elif classe == Grifo:
                
                tamagoshi.tempoPassando()

                acao = input(f"\nDigite sua ação: \n"
                                    f"[1] - Alimentar\n" 
                                    f"[2] - Brincar\n" 
                                    f"[3] - Beber Poção\n"
                                    f"[4] - Estudar\n"
                                    f"[5] - Utilizar Axii\n"
                                    f"[6] - Sair\n"
                                )
                
                passarTempo()
                
                if acao == "1":
                        tamagoshi.alimentar()

                elif acao == "2":
                        tamagoshi.brincar()

                elif acao == "3":
                        tamagoshi.beberPocao()
                    
                elif acao == "4":
                        tamagoshi.estudar()
                    
                elif acao == "5":
                        tamagoshi.utilizarAxii()

                elif acao == "6":
                        print("Você saiu do programa!")
                        break

                tamagoshi.getStatus()

                tamagoshi.getHumor()


            if (tamagoshi.saude == 0 or tamagoshi.saude < 0):
                print(f"{tamagoshi.nome} está muerto T_T!")
                break

            if (tamagoshi.saude < 30):
                print(f"{tamagoshi.nome} estas a morer!")


main()

    



