def positiivisten_summa(lista = list):
    lista = sorted(lista)
    destroy = []
    for i in lista:
        if i < 0:
            destroy.append(i)
    for j in destroy:
        if j < 0:
            lista.remove(j)
    return sum(lista)
if __name__ == "__main__":
    lista = [1, -1, 2, -2, 3, -3]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)

