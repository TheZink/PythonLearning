def poista_isot(lista=list):
    new = []
    for i in lista:
        if i.isupper() == False:
            new.append(i)
    return new

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)
