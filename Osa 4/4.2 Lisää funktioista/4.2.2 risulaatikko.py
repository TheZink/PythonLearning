def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0:1] * x)

def risulaatikko(korkeus):
    while korkeus > 0:
        viiva(10, "#")
        korkeus -= 1