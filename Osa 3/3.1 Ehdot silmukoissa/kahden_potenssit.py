#Tee ohjelma, joka tulostaa ensin luvun 1 ja sen jälkeen kerta toisensa jälkeen aina kaksi kertaa suuremman luvun. Ohjelma siis tulostaa luvun kaksi potensseja
#Ohjelman suoritus päättyy, kun on tulostettu luku, joka on korkeintaan käyttäjän syötteen suuruinen. Yhtään käyttäjän syötettä suurempaa lukua ei siis tulosteta!
#Älä käytä tässä tehtävässä while-komennon ehtona arvoa True!

raja = int(input("Mihin asti: "))
luku = 1

while luku <= raja:
    print(luku)
    luku *= 2


