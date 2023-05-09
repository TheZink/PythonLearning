def lyhin(lista=list):
    x = ""
    for i in lista:
        if len(x) == 0:
            x = i
        if len(i) < len(x):
            x = i
    return x

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = lyhin(lista)
    print(tulos)