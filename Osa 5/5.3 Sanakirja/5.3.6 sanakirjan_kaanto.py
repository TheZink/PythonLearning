def kaanna(dictionary: dict):
    new_dict = {}
    for a, b in dictionary.items():
        new_dict[b] = a
    dictionary.clear()
    for c, d in new_dict.items():
        dictionary[c] = d

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)