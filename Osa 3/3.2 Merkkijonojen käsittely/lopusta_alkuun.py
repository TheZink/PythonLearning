mjono = input("Anna merkkijono: ")
index = -1
stop = 0

while len(mjono) > index:
    print(mjono[index])
    index -= 1
    stop += 1

    if len(mjono) == stop:
        break

#Mallivastaus
#mjono = input("Anna merkkijono: ")
#indeksi = -1
#while indeksi >= -len(mjono):
    #print(mjono[indeksi])
    #indeksi -= 1