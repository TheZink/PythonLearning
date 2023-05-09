def vaihteluvali(lista = list):
    return max(lista) - min(lista)

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)