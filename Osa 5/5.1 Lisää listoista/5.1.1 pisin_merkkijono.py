def pisin(jonot: list):
    x = ""
    for i in jonot:
        if len(i) > len(x):
            x = i
    return x

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))