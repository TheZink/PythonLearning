def keskiarvo(lista = list):
    tulos = sum(lista) / len(lista)
    return tulos

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)
