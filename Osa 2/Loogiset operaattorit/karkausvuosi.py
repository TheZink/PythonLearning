x = int(input("Anna vuosi: "))

if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
    print("Vuosi on karkausvuosi.")

else:
    print("Vuosi ei ole karkausvuosi.")

