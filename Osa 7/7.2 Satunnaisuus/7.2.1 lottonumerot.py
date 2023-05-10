from random import sample
def lottonumerot(amount: int, lower: int, upper: int):
    lottery_number = list(range(lower, upper))
    row = sample(lottery_number, amount)
    return sorted(row)



if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero)
