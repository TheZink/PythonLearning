def tuplaa_alkiot(number: list):
    new_list = []
    for elements in number:
        new_list.append(elements*2)
    return new_list

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)