#Kirjoita ohjelma, joka kysyy ensin käyttäjän nimen. Jos nimi on mikä tahansa muu kuin "Jerry", ohjelma kysyy keittoannosten lukumäärän ja kertoo sitten kokonaishinnan.
#Yksi annos maksaa 5,90.

name = input("Mikä on nimesi: ")

if name != "Jerry":
    keitto = int(input("Kuinka monta annosta keittoa: "))
    x = 5.90
    print(f"Kokonaishinta on {keitto*x}")

print("Seuraava!")
