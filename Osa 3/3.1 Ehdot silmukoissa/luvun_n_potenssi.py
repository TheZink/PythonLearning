# Muuta edellistä ohjelmaa siten, että käyttäjä saa määrätä kertoimen 
# (edellisessä ohjelmassa kerroin oli aina 2), eli sen, minkä luvun potensseja ohjelma tulostaa.

raja = int(input("Mihin asti: "))
pot = int(input("Mikä kerroin: "))
luku = 1

while luku <= raja:
    print(luku)
    luku *= pot

