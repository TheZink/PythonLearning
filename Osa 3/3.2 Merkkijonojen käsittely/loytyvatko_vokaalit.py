word = input("Anna merkkijono: ")
vocals = "aeo"
index = 0

while index < len(vocals):
    vocal = vocals[index]
    if vocal in word:
        print(vocal, "löytyy")
    else:
        print(vocal, "ei löydy")
    index += 1
    