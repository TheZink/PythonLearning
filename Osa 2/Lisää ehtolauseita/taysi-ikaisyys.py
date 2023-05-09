#Tee ohjelma, joka kysyy käyttäjän ikää ja kertoo, onko tämä täysi-ikäinen (eli 18-vuotias tai vanhempi).

x = 18
ika = int(input("Kuinka vanha olet? "))

if ika < x:
    print("Et ole täysi-ikäinen!")

else:
    print("Olet täysi-ikäinen!")