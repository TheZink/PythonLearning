x = input("Salasana: ")

while True:
    y = input("Toista salasana: ")
    if y != x:
        print("Ei ollut sama!")
    else:
        break
print("Käyttäjätunnus luotu!")