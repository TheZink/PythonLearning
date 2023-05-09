def pisin_naapurijono(lista):
    new_list = []
    for i in range(len(lista)):
        if abs(lista[i-1] - lista[i]) == 1 and i < len(lista)-1:
            new_list.append(lista[i])
    return new_list


if __name__ == "__main__":
    lista = [1, 2, 5, 4, 3, 4]
    print(pisin_naapurijono(lista))