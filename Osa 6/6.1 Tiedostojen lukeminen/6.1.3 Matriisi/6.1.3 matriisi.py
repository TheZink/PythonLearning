def summa():
    main_matrix = []
    with open("matriisi.txt") as file:
        for row in file:
            row.replace("\n", "")
            item = row.split(",")
            for a in item:
                main_matrix.append(a)
    math = 0
    for a in main_matrix:
        math += int(a)
    print(math)
    return math
def maksimi():
    main_matrix = []
    with open("matriisi.txt") as file:
        for row in file:
            row.replace("\n", "")
            item = row.split(",")
            for a in item:
                main_matrix.append(a)   
    maks = 0
    for a in main_matrix:
        a = int(a)
        if a > maks:
            maks = a
    print(maks)
    return maks
def rivisummat():
    list1 = []
    with open("matriisi.txt") as file:
        for row in file:
            row.replace("\n", "")
            item = row.split(",")
            math = 0
            for b in item:
                b = int(b)
                math += b
            list1.append(math)
    print(list1)
    return list1

if __name__ == "__main__":
    summa()
    maksimi()
    rivisummat()