numb = [1, 2, 3, 4, 5]

while True:
    a = int(input("Anna indeksi: "))
    if a == -1:
        break
    b = int(input("Anna arvo: "))
    numb[a] = b
    print(numb)