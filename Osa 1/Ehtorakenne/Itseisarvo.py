#Kirjoita ohjelma, joka lukee käyttäjältä kokonaisluvun. Mikäli luku on pienempi kuin 0, ohjelma tulostaa luvun kerrottuna luvulla -1.
#Muulloin ohjelma tulostaa käyttäjän syöttämän luvun

luku = int(input("Anna luku: "))

if luku < 0:
    print(f"Luvun itseisarvo on {luku*-1}")

if luku > 0:
    print(f"Luvun itseisarvo on {luku}")

if luku == 0:
    print(f"Luvun itseisarvo on {luku}")