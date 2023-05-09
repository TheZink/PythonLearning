#Seuraavassa ohjelmassa on useita syntaksivirheitä. Korjaa ohjelma siten, että syntaksi on kunnossa ja se toimii

luku = int(input("Anna luku: "))

if luku>100:
    print("Luku oli suurempi kuin sata")
    luku -= 100
    print("Nyt luvun arvo on pienentynyt sadalla")
    print("Arvo on nyt", luku)
 
print(luku , " taitaa olla onnenlukuni!")
print("Hyvää päivänjatkoa!")