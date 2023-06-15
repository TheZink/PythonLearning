from string import ascii_uppercase

def place(letter, value):
    letter = int(value)
    return letter

def increase(key_value, add_value):
    math = key_value + add_value
    return math

def decrease(key_value, down_value):
    math = key_value - down_value
    return math

def multiplication(key_value, mult_value):
    math = key_value * mult_value
    return math

def statement(a,operand,b):
    check = 0
    if operand == "==":
        if a == b: check = 1
    if operand == "!=":
        if a != b: check = 1
    if operand == "<":
        if a < b: check = 1
    if operand == "<=":
        if a <= b: check = 1
    if operand == ">":
        if a > b: check = 1
    if operand == ">=":
        if a >= b: check = 1
    return check

def suorita(programm: list):
    dictionary, result, location = {}, [], 0
    run, run_timer = True, 0

    for key in ascii_uppercase: #Lisää tyhjät avaimet (A-Z) kirjastoon
        dictionary[key] = 0
    
    while run is True:
        for number in range(location, len(programm)):
            row = programm[number].split() #Funktio purkaa komennot osiin
            run_timer += 1
            
            if row[0] == "MOV": #Lisää kirjastoon uuden avaimen sekä arvon
                if row[2] in ascii_uppercase:
                    create_key = place(row[1], dictionary[row[2]]) 
                else:
                    create_key = place(row[1], int(row[2]))
                dictionary[row[1]] = create_key

            elif row[0] == "ADD": #Laskee nykyisen avaimen arvon ja annetun arvon yhteen sekä päivittää sen avaimeen
                if row[2] in ascii_uppercase:
                    add_value = increase(dictionary[row[1]], dictionary[row[2]])
                else:
                    add_value = increase(dictionary[row[1]], int(row[2]))
                dictionary[row[1]] = add_value
            
            elif row[0] == "SUB": #Vähentää nykyisen avaimen arvon annetulla arvolla sekä päivittää sen avaimeen
                if row[2] in ascii_uppercase:
                    down_value = decrease(dictionary[row[1]], dictionary[row[2]])
                else:
                    down_value = decrease(dictionary[row[1]], int(row[2]))
                dictionary[row[1]] = down_value
            
            elif row[0] == "MUL": #Kertoo nykyisen avaimen arvon annetulla arvolla sekä päivittää sen avaimeen
                if row[2] in ascii_uppercase:
                    multi_value = multiplication(dictionary[row[1]], dictionary[row[2]])
                else:
                    multi_value = multiplication(dictionary[row[1]], int(row[2]))
                dictionary[row[1]] = multi_value
            
            elif row[0] == "PRINT": #Komento lisää annetun avaimen arvon result-listaan
                if row[1] in dictionary:
                    result.append(dictionary[row[1]])
                else:
                    result.append(int(row[1]))
            
            elif row[0] == "IF": #Funktiossa toteutetaan annettu IF-lausekkeen. Mikäli ehto toteutuu, ajetaan lausekkeen käsky
                if row[3] in dictionary:
                    check = statement(dictionary[row[1]], row[2], dictionary[row[3]])
                elif row[3] not in dictionary:
                    check = statement(dictionary[row[1]], row[2], int(row[3]))

                if check == 1:
                    location = programm.index(f"{row[5]}:")
                    run_timer = programm.index(f"{row[5]}:")
                    break
                else:
                    continue

            elif row[0] == "JUMP": #Hypätään komennossa olevaan kohtaan
                location = programm.index(f"{row[1]}:")
                run_timer = programm.index(f"{row[1]}:")
                break

            elif "END" in row:
                run = False
                break

            elif number == len(programm):
                run = False
                break

        # if result == result4: #Debuggaus funktio
        #     print(f"Rivi: {row}")
        #     print(number)
        #     print(f"Ollaan {run_timer} timerissä, kun ohjelman pituus on {len(programm)}")
        #     print(result)
        #     breakpoint()

        if run_timer == len(programm): #Jos ohjelma on ajettu loppuun, mennään tähän
            run = False
            break
        
    return result

if __name__ == "__main__":
    program6 = ["MOV N 100","PRINT 2","MOV A 3","alku:","MOV B 2","MOV Z 0","testi:","MOV C B","uusi:","IF C == A JUMP virhe","IF C > A JUMP ohi","ADD C B","JUMP uusi","virhe:","MOV Z 1","JUMP ohi2","ohi:","ADD B 1","IF B < A JUMP testi","ohi2:","IF Z == 1 JUMP ohi3","PRINT A","ohi3:","ADD A 1","IF A <= N JUMP alku"]

    tulos = suorita(program6)
    print(tulos)
