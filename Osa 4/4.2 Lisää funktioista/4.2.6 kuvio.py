def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0:1] * x)
    
def kuvio (a, b, c, d):
    time1 = a
    time2 = c
    i = 1
    while time1 > 0:
        viiva(i, b)
        time1 -= 1
        i += 1
    while time2 > 0:
        viiva(a, d)
        time2 -= 1

if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
