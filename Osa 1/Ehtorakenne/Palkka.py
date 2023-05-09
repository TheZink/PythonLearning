#Tee ohjelma, joka kysyy tuntipalkkaa, työskenneltyjen tuntien määrää ja viikonpäivää. 
#Ohjelma tulostaa palkan, joka on tuntipalkka kertaa tuntien määrä muina päivinä paitsi sunnuntaisin, jolloin tuntipalkka on kaksinkertainen.

palk = float(input("Tuntipalkka: "))
work = float(input("Työtunnit: "))
day = input("Viikonpäivä: ")

x = palk*work
y = (palk*2)*work

if day != "sunnuntai":
    print(f"Palkka {x} euroa")

else:
    print(f"Palkka {y} euroa")

#elif day == "sunnuntai":
    #print(f"Palkka {y} euroa")