word = input("Sana: ")
sign = input("Merkki: ")
x = word.find(sign)
y = x + 3

while y < len(word):
    if sign in word:
        print(word[x:y])
        break
    else:
        break