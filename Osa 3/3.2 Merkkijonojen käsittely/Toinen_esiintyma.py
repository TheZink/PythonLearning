mjono = input("Anna merkkijono: ")
ojono = input("Anna osajono: ")
x = mjono.find(ojono)
y = mjono[x+len(ojono):].find(ojono)
z = x + y + len(ojono)

if y > 1:
    print(f"Osajonon toinen esiintymä on kohdassa {z}.")
else:
    print("Osajono ei esiinny merkkijonossa kahdesti.")
