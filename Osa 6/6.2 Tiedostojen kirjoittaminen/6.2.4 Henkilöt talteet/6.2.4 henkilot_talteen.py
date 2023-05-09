def tallenna_henkilo(person: tuple):
    with open("henkilot.csv", "a") as file:
        file.write(f"{person[0]};{person[1]};{person[2]}\n")

if __name__ == "__main__":
    tallenna_henkilo(("Kimmo testinen",40,175.5))

