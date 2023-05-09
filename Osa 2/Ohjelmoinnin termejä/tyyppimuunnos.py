#Pythonissa voidaan usein muuntaa jokin arvo tyypistä toiseen. Esimerkiksi liukuluku voidaan muuntaa kokonaisluvuksi funktion "int" avulla
#Tee int-funktiota hyödyntäen ohjelma, joka kysyy käyttäjältä desimaaliluvun ja tulostaa erikseen luvun kokonaisosan ja desimaaliosan.
#Huom! Voit olettaa, että annettu desimaaliluku on suurempi kuin nolla.

luku = float(input("Anna luku: "))

x = int(luku)
y = luku-x

print(f"Kokonaisosa: {x}")
print(f"desimaaliosa: {y}")