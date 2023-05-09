maara = 0
summa = 0
kopio = ""
pos = 0
neg = 0
while True:
    numb = int(input("Syötä kokonaislukuja, 0 lopettaa: "))
    maara += 1
    summa += numb
    if numb == 0 or numb == kopio:
        maara -= 1
        break
    if numb >= 0:
        pos += 1
    elif numb <= 0:
        neg += 1
    keski = summa / maara
print("Syötä kokonaislukuja, 0 lopettaa: ")
print("Lukujen kysely")
print(f"Lukuja yhteensä {maara}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {keski}")
print(f"Positiivisia {pos}")
print(f"Negatiivisia {neg}")