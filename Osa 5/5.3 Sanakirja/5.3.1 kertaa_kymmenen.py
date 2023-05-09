def kertaa_kymmenen(a: int, b: int):
    numbers = {}
    for c in range(a,b+1):
        numbers[c] = c * 10
    return numbers

if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)
