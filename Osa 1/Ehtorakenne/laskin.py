#Tee ohjelma, joka kysyy käyttäjältä ensin kaksi lukua ja sen jälkeen komennon.
#Jos komento on joko summa, tulo tai erotus, ohjelma laskee syötteille kyseisen operaation tuloksen. Muussa tapauksessa ohjelma ei tulosta mitään.

luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
cmd = input("Komento: ")

if cmd == "summa":
    print(f"{luku1} + {luku2} = {luku1+luku2}")

elif cmd == "tulo":
    print(f"{luku1} * {luku2} = {luku1*luku2}")

elif cmd == "erotus":
    print(f"{luku1} - {luku2} = {luku1-luku2}")

else:
    print("Ole hyvä ja määritä komento. Komennot: summa, tulo tai erotus. Muista kirjoittaa komennot pienillä kirjaimilla")
    print("Kiitos!")