#Jos print-komennolle annetaan lisäparametri end = "", komento ei tulosta rivinvaihtoa merkkijonon jälkeen.
#Korjaa ohjelma niin, että koko lasku tuloksineen tulostetaan yhdelle riville muuttamatta kuitenkaan print-komentojen määrää:

# Korjaa ohjelma
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4, end="")
