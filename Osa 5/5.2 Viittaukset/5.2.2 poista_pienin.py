def poista_pienin(luvut: list):
    smaller = luvut[:]
    smaller.sort()
    luvut.remove(smaller[0])

if __name__ == "__main__":
    luvut = [2, 4, 6, 6, 3, 5]
    poista_pienin(luvut)
    print(luvut)