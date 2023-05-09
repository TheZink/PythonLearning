#Tee ohjelma, joka lukee käyttäjältä neljä lukua ja tulostaa niiden summan ja keskiarvon

luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
luku3 = int(input("Luku 3: "))
luku4 = int(input("Luku 4: "))

summa = luku1 + luku2 + luku3 + luku4
jako = summa / 4

print(f"Lukujen summa on {summa} ja keskiarvo {jako}")