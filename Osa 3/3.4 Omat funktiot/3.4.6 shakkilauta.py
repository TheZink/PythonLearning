def shakkilauta(x):
    time = x
    z = "10" * x
    while time > 0:
        print(z[0:x])
        z = z[1:]
        time -= 1
if __name__ == "__main__":
    shakkilauta(30)