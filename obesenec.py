"""
Obesenec
1. ziskej nahodne slovo
2. prevod slova na pismena
3. misto kam ulozit uhadnute a neuhadnute pismena
4. zjisteni vyskitu ve slove
6. osetrit vstup - pouze pismena z abecedy
"""

import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


with open("words.txt", "r") as f:
    slova = f.read()
    slova = slova.split("\n")


lehka_slova = slova[0].split(" ")
stredni_slova = slova[1].split(" ")
tezka_slova = slova[2].split(" ")
stats = {"vyhry": 0, "prohry": 0, "uhadnute": 0, "chybne": 0}
obtiznost = 1
game = True
zivoty = 5

while game:
    clear()
    print("########################################")
    print("###             Hangman              ###")
    print("########################################")
    print("")
    print("Hrát (h/H)")
    print("statistiky (s/S)")
    print("Nastavení (n/N)")
    print("Konec (k/K)")
    x = input("=>")
    x = x.lower()[0]

    if x == "h":
        clear()
        print("")
        print("")
        print("############ Hra začíná ###########")
        print("")
        print("")
        gameLoop = True
        if obtiznost == 0:
            slova = lehka_slova
            zivoty = 10
        elif obtiznost == 1:
            slova = stredni_slova
            zivoty = 5
        elif obtiznost == 2:
            slova = tezka_slova
            zivoty = 5
        else:
            clear()
            print("Error: chybne nastavena obtiznost")
            gameLoop = False

        slovo = random.choice(slova)
        slovo = list(slovo)
        pocet_pismen = 0
        uhadnute = []
        chybne = []
        while gameLoop:
            if pocet_pismen == len(slovo):
                uhadnute_slovo = ""
                for i in slovo:
                    uhadnute_slovo += i
                clear()
                print("Vyhrál jsi, hádané slovo bylo:", uhadnute_slovo)
                stats["vyhry"] += 1
                gameLoop = False
                input("\n pro pokračování zmáčkněte ENTER")
            elif zivoty <= 0:
                clear()
                print("Prohrál jsi")
                stats["prohry"] += 1
                gameLoop = False
                input("\n pro pokračování zmáčkněte ENTER")
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
                if check:
                    check = False
                    for i in uhadnute:
                        if pismeno == i:
                            check = True
                    if check:
                        clear()
                        print(pismeno, "jsi už hádal")
                    else:
                        uhadnute.append(pismeno)
                        clear()
                        print(pismeno, "je v hádaném slově", count, "krát")
                        stats["uhadnute"] += 1
                        pocet_pismen += count
                else:
                    check = False
                    for i in chybne:
                        if pismeno == i:
                            check = True
                    if check:
                        clear()
                        print(pismeno, "jsi už hádal")
                    else:
                        chybne.append(pismeno)
                        clear()
                        print(pismeno, "se v hádaném slově nenachází")
                        stats["chybne"] += 1
                        zivoty -= 1
                nahoda = ""
                for i in slovo:
                    if i in uhadnute:
                        nahoda += i
                    else:
                        nahoda += "_"
                print(nahoda)
                print("životy:", zivoty)
                print("")
                print("===============================")
                print("")
    elif x == "n":
        nastaveni = True
        while nastaveni:
            clear()
            print("Nastaveni:")
            print("  -> Obtížnosti (o/O)")
            print("  -> Exit (e/E)")
            x = input("=>")
            x = x.lower()[0]
            if x == "o":
                clear()
                print("Obtížnost")
                print("  -> Lehká (0)")
                print("  -> Střední (1)")
                print("  -> Těžká (2)")
                x = input("=>")
                if x.isnumeric():
                    x = int(x)
                if x == 0:
                    obtiznost = 0
                    print("přenastavil jsi obtížnost na: Lehká")
                    input("\npro pokračování zmáčkněte ENTER")
                elif x == 1:
                    obtiznost = 1
                    print("přenastavil jsi obtížnost na: Střední")
                    input("\npro pokračování zmáčkněte ENTER")
                elif x == 2:
                    obtiznost = 2
                    print("přenastavil jsi obtížnost na: Těžká")
                    input("\npro pokračování zmáčkněte ENTER")
                else:
                    print("Daná obtížnost neexistuje!!!")
                    input("\n pro pokračování zmáčkněte ENTER")
            elif x == "e":
                nastaveni = False
    elif x == "s":
        clear()
        print("Statistiky")
        print("  -> Vyhry/Prohry")
        print("    -> ", stats["vyhry"], "/", stats["prohry"], sep="")
        print("  -> Uhadnute/Chybne")
        print("    -> ", stats["uhadnute"], "/", stats["chybne"], sep="")
        input("\npro pokračování zmáčkněte ENTER")
    elif x == "k":
        game = False
    else:
        clear()
        print("Daná možnost neexistuje!!!")
