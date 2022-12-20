"""
Obesenec
1. ziskej nahodne slovo
2. prevod slova na pismena
3. misto kam ulozit uhadnute a neuhadnute pismena
4. zjisteni vyskitu ve slove
6. osetrit vstup - pouze pismena z abecedy
"""

import random

gameLoop = True
slova = ["auto", "kolo", "paprika"]


while gameLoop:
    slovo = random.choice(slova)
    slovo = list(slovo)
    pocet_pismen = 0
    zivoty = 5
    uhadnute = []
    chybne = []
    while gameLoop:
        if pocet_pismen == len(slovo):
            uhadnute_slovo = ""
            for i in slovo:
                uhadnute_slovo += i
            print("Vyhrál jsi, hádané slovo bylo:", uhadnute_slovo)
            gameLoop = False
        elif zivoty <= 0:
            print("Prohrál jsi")
            gameLoop = False
        else:
            print("hádaný znak")
            pismeno = input("=>")
            pismeno = pismeno.lower()[0]
            check = False
            count = 0
            for i in slovo:
                if pismeno == i:
                    check = True
                    count += 1
                    pocet_pismen += 1
            if check == True:
                uhadnute.append(pismeno)
                print(pismeno, "je v hádaném slově", count,"krát")
            else:
                chybne.append(pismeno)
                print(pismeno, "se v hádaném slově nenachází")
                zivoty -= 1
            nahoda = ""
            for i in slovo:
                if i in uhadnute:
                    nahoda += i
                else:
                    nahoda += "_"
            print(nahoda)
            print("životy:", zivoty)