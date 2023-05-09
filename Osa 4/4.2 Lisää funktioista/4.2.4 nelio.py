def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0:1] * x)

def nelio(koko, merkki):
    time = koko
    while time > 0:
        viiva(koko, merkki)
        time -= 1

