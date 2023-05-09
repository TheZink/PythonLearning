def vanhin(person: list):
    old = 2023
    name = ""
    for older in person:
        if older[1] < old:
            old = older[1]
            name = older[0]
    return name 


if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))