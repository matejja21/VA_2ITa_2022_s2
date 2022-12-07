
def prvocislo(num):
    if num > 1:
        check = 0
        for i in range(num):
            i = i + 1
            if (num % i) == 0:
                check = check + 1
        if check == 2:
            return True
        else:
            return False
    else:
        return False


# print(prvocislo(18))

# list_a = []
# list_b = list()

# seznam_cisel = [6, 4, 8, 9, 64, 75, 41, 49, 51, 57, 698, 571]
#
# for num in seznam_cisel:
#     print(num, prvocislo(num))
#
# for index in range(len(seznam_cisel)):
#     print(index, seznam_cisel[index], prvocislo(seznam_cisel[index]))
#
#
# telefony = [
#     "Apple",
#     "Samsung",
#     "Xiaomi",
#     "Nokia",
#     "Sony",
#     "Huawei",
#     "Google",
# ]
#
# print(telefony[2])
# telefony[2] = "Pocophone"
# # telefony[7] = "Ericsson"
# telefony.insert(7, "Ericsson")
# telefony.append("Asus")
# telefony.insert(len(telefony), "Vodafone")
# print(telefony)
# print(telefony[-5])
# del telefony[0]
# print(telefony)
# telefony.remove("Ericsson")
# print(telefony)
#
#
#
#
# prvocisla = []
# for n in range(1000):
#     if prvocislo(n):
#         prvocisla.append(n)
#
# # List comprehension
#
# posloupnost = [x for x in range(1000)]
# prvoci = [n for n in posloupnost if prvocislo(n)]
#
# binarka = [2 ** b for b in posloupnost]



# for x in range(1, 5):
#     for y in range (1, 5):
#         print(x * y, end=" ")
#     print()


nasobky = [[x * y for y in range(1,5)] for x in range(1,5)]
for radek in nasobky:
    print(radek)

print("STOP")