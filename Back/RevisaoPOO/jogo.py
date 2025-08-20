import random

from tamagoshi import Tamagoshi
from lobo import Lobo
from urso import Urso
from grifo import Grifo

while True:
    escolha_classe = int(input(f"Qual classe você quer utilizar: \n"
                                f"[1] - Lobo\n"
                                f"[2] - Urso\n"
                                f"[3] - Grifo\n"
                                f"[4] - Aleatória\n"))
    
    

    if escolha_classe == 4:
        print("Você escolheu uma classe aleatória, logo aparecerá qual é a sua classe.")
        escolha_classe = random.randint(1,3)

    if escolha_classe == 1:
        print("Sua classe é LOBO")
        classe = Lobo
        break
    elif escolha_classe == 2:
        print("Sua classe é URSO")
        classe = Urso
        break
    elif escolha_classe == 3:
        print("Sua classe é GRIFO")
        classe = Grifo
        break
    else:
        print("Atenção! O digito não corresponde a nenhuma classe!")


