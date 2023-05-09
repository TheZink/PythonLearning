def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0:1] * x)

def risunelio(koko):
    time = koko
    while time > 0:
        viiva(koko, "#")
        time -= 1

if __name__ == "__main__":
    risunelio(3)
