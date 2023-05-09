#Tee ohjelma, joka kysyy käyttäjältä sanaa ja tulostaa sanan tähtiraameihin, joissa sana on keskellä.
#Raamien leveys on 30 merkkiä, ja voit olettaa, että sana mahtuu raameihin.
#Huom! Jos sanan pituus on pariton, voit tulostaa sanan kumpaan tahansa mahdollisista keskikohdista.

word = input("Sana: ")
jako1 = (28 - len(word)) // 2
jako2 = (28 - len(word)) // 2
space1 = " " * jako1
space2 = " " * jako2

if len(word) % 2 == 0:
    print("*" * 30)
    print("*" + space1 + word + space1 + "*")
    print("*" * 30)
else:
    print("*" * 30)
    print("*" + space2 + word + space2 + " " + "*")
    print("*" * 30) 
