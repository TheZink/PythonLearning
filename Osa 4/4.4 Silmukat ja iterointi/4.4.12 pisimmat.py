def pisimmat(lista=list):
    x = ""
    pisin = []
    for i in lista:
        if len(i) >= len(x) or len(x) == 0:
            x = i
    for i in lista:
        if len(x) == len(i):
            pisin.append(i)
    return pisin

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos) # ['seitsemäs']