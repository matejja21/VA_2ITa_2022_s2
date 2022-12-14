#
# def vypocti_plochu(a, b=0):
#     if b == 0:
#         return a * a
#     else:
#         return a * b
#
# print(vypocti_plochu(5, 2))
#
#
# def new_print(*cisla, limit):
#     #  for cislo in cisla:
#     #    print(cislo)
#     i=0
#     while i == limit:
#         print(cisla[i])
#         i += 1
#
#
# new_print(1, 2, 3, 4, 5, 6, 7, 8, 9, limit=3)


# def F(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return F(n - 1) + F(n - 2)
#
# i = 0
# while True:
#     print(i, F(i))
#     i+=1

# vstup = [1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
# def nacti(vstup, num):
#     return vstup[num]
#
# def Alik(num=0):
#     i = nacti(vstup, num)
#     num += 1
#     if i == 0:
#         i = nacti(vstup, num)
#         num += 1
#     else:
#         if i > 5:
#             i = nacti(vstup, num)
#             num += 1
#             num = Alik(num)
#             i = nacti(vstup, num)
#             num += 1
#         else:
#             num = Alik(num)
#             i = nacti(vstup, num)
#             num += 1
#             i = nacti(vstup, num)
#             num += 1
#     return num
#     print(i)
#
# Alik()

import random

gameLoop = True

while gameLoop:
    tahy_pocitace = ["k", "n", "p"]
    tah_pc = random.choice(tahy_pocitace)

    print("(k)kámen, (n)nůžky, (p)papír")
    tah_hrace = input("=>")
    tah_hrace = tah_hrace.lower()[0]

    if tah_hrace == "k":
        if tah_pc == "k":
            print("remiza")
        elif tah_pc == "n":
            print("vyhra")
        elif tah_pc == "p":
            print("prohra")
    elif tah_hrace == "n":
        if tah_pc == "n":
            print("remiza")
        elif tah_pc == "p":
            print("vyhra")
        elif tah_pc == "k":
            print("prohra")
    elif tah_hrace == "p":
        if tah_pc == "p":
            print("remiza")
        elif tah_pc == "k":
            print("vyhra")
        elif tah_pc == "n":
            print("prohra")


