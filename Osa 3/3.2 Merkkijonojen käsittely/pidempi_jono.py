sana1 = input("Anna jono 1: ")
sana2 = input("Anna jono 2: ")

x = len(sana1)
y = len(sana2)

if x > y:
    print(f"{sana1} on pidempi")
elif y > x:
    print(f"{sana2} on pidempi")
else:
    print("Jonot ovat yhtä pitkät")