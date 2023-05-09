def luvuista_suurin(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    suurin = luvuista_suurin(3, 5, 6)
    print(suurin)