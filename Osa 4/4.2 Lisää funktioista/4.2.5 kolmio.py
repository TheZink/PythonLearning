def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0:1] * x)

def kolmio(koko):
    time = koko
    z = 1
    while time > 0:
        viiva(z, "#")
        time -= 1
        z += 1


