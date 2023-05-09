def booking():
    while True:
        print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
        choose = int(input("Valinta: "))
        if choose == 1:
            add = input("Anna merkintä: ")
            with open("paivakirja.txt", "a") as file:
                file.write(f"{add}\n")
        if choose == 2:
            with open("paivakirja.txt") as file:
                for diary in file:
                    print(diary)
        if choose == 0:
            print("Heippa!")
            break

booking()