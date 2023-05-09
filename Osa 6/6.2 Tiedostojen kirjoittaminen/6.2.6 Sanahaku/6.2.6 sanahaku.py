from string import ascii_lowercase
def hae_sanat(search: str):
    words = []
    
    with open("sanat.txt") as file:
        for text in file:
            text = text.strip()
            if search == text:
                words.append(text)
            if search.startswith("*") == True: #Jos *-merkki on hakusanan alussa, etsitään tiedostossa hakusanan loppuosat
                clean = search.replace("*", "")
                if text.endswith(clean) == True:
                    words.append(text)
            if search.endswith("*") == True: #Jos *-merkki on hakusanan lopussa, etsitään tiedostosta hakusanan alkuosat
                clean = search.replace("*", "")
                if text.startswith(clean) == True:
                    words.append(text)
            if "." in search: #Jos hakusanassa on jokerit, funktio käy kirjaimet kerrallaan ja etsii sopivat sanat
                check = ""
                if len(search) == len(text):
                    for time in range(0, len(search), 1):
                        if search[time] == text[time]:
                            check += text[time]
                        if search[time] == ".":
                            check += text[time]
                        if check == text:
                            words.append(check)

    return words

if __name__ == "__main__":            
    hae_sanat("z.ne.")