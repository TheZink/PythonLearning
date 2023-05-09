def uusi_henkilo(name: str, age: int):
    if name == "": raise ValueError("nimi on tyhjä merkkijono")
    if len(name.split()) < 2: raise ValueError("nimi ei koostu vähintään kahdesta sanasta")
    if len(name) > 40: raise ValueError("nimen pituus on yli 40 merkkiä")
    if age < 0: raise ValueError("ikä on negatiivinen luku")
    if age > 150: raise ValueError ("ikä on suurempi kuin 150")

    return (name, age)

if __name__ == "__main__":
    person = uusi_henkilo("", 150)