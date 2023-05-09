#Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten kaikki sen
#ensimmäisestä merkistä alkavat osajonot pituusjärjestyksessä.
word = input("Anna merkkijono: ")
x = 0

while x <= len(word):
    print(word[0:x])
    x += 1

