def pisin_naapurijono(my_list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
            
            
    return longest


if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))


    #    for i in range(0, len(lista)):
    #     if abs(lista[i] - lista[i-1]) == 1 or abs(lista[i] - lista[i+1]) == 1:
    #         new_list.append(lista[i])
    # return new_list