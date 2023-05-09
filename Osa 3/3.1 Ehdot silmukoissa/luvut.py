#Tee ohjelma, joka tulostaa kaikki käyttäjän antamaa lukua pienemmät luvut alkaen luvusta yksi.
#Älä käytä tässä tehtävässä while-komennon ehtona arvoa True!

raja = int(input("Mihin asti: "))
luku = 1

while luku < raja:
    print(luku)
    luku += 1