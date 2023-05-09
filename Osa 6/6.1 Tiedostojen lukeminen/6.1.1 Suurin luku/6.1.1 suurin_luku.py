def suurin():
    with open("luvut.txt") as file:
        high = 0
        for column in file:
            number = int(column)
            if number > high:
                high = number
    return high

if __name__ == "__main__":
    suurin()