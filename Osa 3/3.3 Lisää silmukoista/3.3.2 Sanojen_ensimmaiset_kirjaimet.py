sana = input("Anna lause: ")
merkki = " "
print(sana[0:1])

while True:
    x = sana.find(merkki)
    if len(sana) < 3:
        break
    elif sana[0] == merkki:
        print(sana[x+1:2])
    sana = sana[1:]