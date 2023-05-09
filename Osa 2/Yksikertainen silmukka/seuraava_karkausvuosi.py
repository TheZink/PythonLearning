year = int(input("Vuosi: "))
leap = year

while True:
    leap += 1
    if leap % 4 == 0 and (leap % 100 != 0 or leap % 400 == 0):
        break
    elif leap % 100 != 0 and leap % 400 == 0:
        break

print(f"Vuotta {year} seuraava karkausvuosi on {leap}")
