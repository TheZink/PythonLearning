def histogrammi(a):
    dictionary = {}
    for b in a:
        if b not in dictionary:
            dictionary[b] = "*"
        else:
            dictionary[b] += "*"
    for c in dictionary:
        print(c,dictionary[c])

if __name__ == "__main__":
    histogrammi("saippuakauppias")

