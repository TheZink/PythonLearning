#Tee ohjelma, joka kysyy kahden henkilön nimen ja iän ja tulostaa vanhemman henkilön nimen

print("Henkilö 1:")
nimi1 = input("Nimi: ")
ika1 = int(input("Ikä: "))

print("Henkilö 2:")
nimi2 = input("Nimi: ")
ika2 = int(input("Ikä: "))

if ika1 > ika2:
    print(f"Vanhempi on {nimi1}")

elif ika2 > ika1:
    print(f"Vanhempi on {nimi2}")

else:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")