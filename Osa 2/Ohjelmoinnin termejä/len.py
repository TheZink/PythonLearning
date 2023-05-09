#Funktiolla len voidaan laskea (muun muassa) merkkijonon pituus. Funktio palauttaa merkkijonossa olevien merkkien määrän.
#Tee ohjelma, joka lukee käyttäjältä sanan ja tulostaa sanan merkkien määrän, mikäli niitä on enemmän kuin yksi

sana = input("Anna sana: ")
x = len(sana)

if x > 1:
    print(f"Sanassa {sana} on {x} kirjainta")

print("Kiitos!")