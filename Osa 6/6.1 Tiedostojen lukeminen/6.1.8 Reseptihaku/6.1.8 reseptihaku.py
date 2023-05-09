def converter(file: str):
    recept1 = {}
    with open(f"{file}") as file:
        time = 0
        title = ""
        for ingredient in file:
            if time == 0: 
                title = ingredient.strip()
                time += 1
            elif time == 1: 
                recept1[title] = [int(ingredient.strip())]
                time += 1
            elif time == 2: 
                if ingredient == "\n": 
                    time = 0
                else: 
                    recept1[title].append(ingredient.strip())
    return recept1

def hae_nimi(file: str, name: str):
    recept = converter(file)
    find = []
    for a in recept:
        if name.lower() in a.lower():
            find.append(a)
    return find

def hae_aika(file: str, time: int):
    recept = converter(file)
    cooking_time = []
    for a, b in recept.items():
        c = int(b[0])
        if time >= c:
            cooking_time.append(f"{a}, valmistusaika {b[0]} min")
    return cooking_time

def hae_raakaaine(file: str, material: str):
    recept = converter(file)
    find = []
    for a, b in recept.items():
        if material in b:
            find.append(f"{a}, valmistusaika {b[0]} min")
    return find
            

if __name__ == "__main__":
    loydetyt = hae_nimi("reseptit1.txt", "pulla")
    for resepti in loydetyt:
        print(resepti)
    loydetyt = hae_aika("reseptit1.txt", 30)
    for resepti in loydetyt:
        print(resepti)
    loydetyt = hae_raakaaine("reseptit1.txt", "maito")
    for resepti in loydetyt:
        print(resepti)