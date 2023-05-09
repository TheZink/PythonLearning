def pisimman_pituus(lista = list):
    x = ""
    for i in lista:
        if len(i) > len(x):
            x = i
    return len(x)

if __name__ == "__main__":
    lista = ["arto", "Matti"]
    tulos = pisimman_pituus(lista)
    print(tulos)