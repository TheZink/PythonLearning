dictionary = {}
while True:
    commands = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    if commands == 1:
        a = input("nimi: ")
        if a in dictionary:
            print(dictionary[a])
        else:
            print("ei numeroa")
    if commands == 2:
        b = input("nimi: ")
        c = str(input("numero: "))
        dictionary[b] = c
        print("ok!")
    if commands == 3:
        print("lopetetaan...")
        break