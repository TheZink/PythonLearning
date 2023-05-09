def insertion(): #Funktio lisää syötetyn tekstin "sanakirja.txt" tiedostoon
    FIN = input("Anna sana suomeksi: ")
    ENG = input("Anna sana englanniksi: ")
    with open("sanakirja.txt", "a") as file:
        file.write(f"{FIN};{ENG}\n")
    return

def search(): #Funktio hakee "sanakirja.txt" tiedostosta sopivat sanat syötetyn tekstin kanssa
    word = input("Anna sana: ")
    with open("sanakirja.txt") as file:
        for row in file:
            row = row.split(";")
            if word.lower() in row[0].lower() or word in row[1].lower():
                print(F"{row[0]} - {row[1]}")
    return

def main():
    while True:
        print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
        choice = int(input("Valinta: "))
        if choice == 1:
            insertion()
            print("Sana pari lisätty")
        if choice == 2:
            search()
        if choice == 3:
            print("Moi!")
            break

main()
