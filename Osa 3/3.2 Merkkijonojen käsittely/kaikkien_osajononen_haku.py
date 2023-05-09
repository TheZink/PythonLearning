word = input("Sana: ")
sign = input("Merkki: ")

while True:
    x = word.find(sign)
    if len(word) < 3:
        break
    elif word[0] == sign:
        print(word[x:x+2])
    word = word[1:]