def kertomat(a:int):
    dictionary = {}
    numbers = 1
    for b in range(1, a+1):
        numbers = b * numbers
        dictionary[b] = numbers
    return dictionary

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])