def writing():
    name = input("Kenelle teos omistetaan: ")
    f_name = input("Mihin kirjoitetaan: ")

    with open(f_name, "w") as file:
        file.write(f"Hei {name}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")

writing()