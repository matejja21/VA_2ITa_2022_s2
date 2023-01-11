hodnoty = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
barvy = ("S", "K", "P", "L")

balicek = []
for barva in barvy:
    for hodnota in hodnoty:
        karta = {
            "barva": barva,
            "hodnota": hodnota,
        }
        balicek.add(karta)


balicek