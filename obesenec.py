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
    uhadnute = []
    chybne = []
    while gameLoop:
        print("hádaný znak")
        pismeno = input("=>")
        pismeno = pismeno.lower()[0]
        check = False
        count = 0
        for i in slovo:
            if pismeno == i:
                check = True
                count += 1
        if check == True:
            uhadnute.append(pismeno)
            print(pismeno, "je v hádaném slově", count,"krát")
        else:
            chybne.append(pismeno)
            print(pismeno, "se v hádaném slově nenachází")
        nahoda = ""
        for i in slovo:
            if i in uhadnute:
                nahoda += i
            else:
                nahoda += "_"
        print(nahoda)