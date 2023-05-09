def uniikit(lista = list):
    new_list = []
    for i in lista:
        if i not in new_list:
            new_list.append(i)
    return sorted(new_list)


if __name__ == "__main__":
    lista = [3,2,1,3,2,1,3,2,1]
    vastaus = uniikit(lista)
    print(vastaus) # [1, 2, 3]