from math import sqrt

while True:
    x = float(input("Syötä luku: "))
    if x == 0:
        break
    if x < 0:
        print("Epäkelpo luku")
    else:
        print(sqrt(x))

print("Lopetetaan...")
