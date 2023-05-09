#Tee ohjelma, joka kysyy huomisen sääennusteen ja suosittelee sen mukaista pukeutumista.
#Suositus vaihtelee sen mukaan, onko lämpötila yli 20 astetta, yli 10 astetta vai yli 5 astetta. Myös sade vaikuttaa suositukseen.

print("Kerro huominen sääennuste:")
temp = int(input("Lämpötila: "))
rain = input("Sataako (kyllä/ei): ")

if temp > 20:
    print("Pue housut ja t-paita")

if temp == 20:
    print("Pue housut ja t-paita")
    if rain == "kyllä":
        print("Ota myös pitkähihainen paita")

if temp < 20:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")

if temp < 15:
     print("Pue päälle takki")

if temp == 5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if temp < 5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if rain == "kyllä":
        print("Muista sateenvarjo!")