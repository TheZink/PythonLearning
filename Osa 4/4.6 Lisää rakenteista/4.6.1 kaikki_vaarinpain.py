def kaikki_vaarinpain(lista=list):
    palautus = []
    kaannos = lista[::-1]
    for i in kaannos:
        palautus.append(i[::-1])
    return palautus

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)