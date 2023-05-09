#Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten kaikki sen viimeiseen
#merkkiin päättyvät osajonot pituusjärjestyksessä.

word = input("Anna merkkijono: ")
index = len(word) - 1
stop = 0

while index <= index:
    print(word[index:len(word)])
    index -= 1
    stop += 1

    if stop == len(word):
        break
