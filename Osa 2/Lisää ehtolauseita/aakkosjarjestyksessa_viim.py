#Lukujen lisäksi Python osaa vertailla myös merkkijonojen suuruusjärjestystä.
#Merkkijono a on pienempi kuin merkkijono b, jos merkkijono a tulee aakkosjärjestyksessä ennen jonoa b.
#Huomaa kuitenkin, että tämä pätee varmasti vain kun
#   - vertaillaan samankokoisia kirjaimia (eli ISOJA tai pieniä kirjaimia) keskenään ja
#   - vertailtavissa sanoissa on vain englannin kielestä tuttuja kirjaimia (eli a-z tai A-Z)
#Tee ohjelma, joka kysyy käyttäjältä kahta sanaa. Ohjelma tulostaa sanoista sen, joka on aakkosjärjestyksessä jälkimmäinen.
#Voit olettaa, että sanat on syötetty kokonaan pienillä kirjaimilla.

sana1 = input("Anna 1. sana: ")
sana2 = input("Anna 2. sana: ")

if sana1 > sana2:
    print(f"{sana1} on aakkosjärjestyksessä viimeinen.")

elif sana2 > sana1:
    print(f"{sana2} on aakkosjärjestyksessä viimeinen.")

elif sana1 == sana2:
    print("Annoit saman sanan kahdesti.")
