# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0:1] * x)

