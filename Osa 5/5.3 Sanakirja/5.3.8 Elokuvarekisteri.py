def lisaa_elokuva(rekisteri: list, name: str, director: str, year: str, lenght: int):
    register={"nimi": name, "ohjaaja": director, "vuosi": year, "pituus": lenght}
    rekisteri.append(register)
    
if __name__ == "__main__":
    rekisteri = []
    lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
    lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
    print(rekisteri)