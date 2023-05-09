list = []
while True:
    numb = int(input("Anna luku: "))
    if numb == 0:
        print("Moi!")
        break
    else:
        list.append(numb)
        print(f"Lista: {list}")
        print(f"Järjestettynä: {sorted(list)}")