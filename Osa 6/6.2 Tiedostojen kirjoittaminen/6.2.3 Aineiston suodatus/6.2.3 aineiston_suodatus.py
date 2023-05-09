def suodata_laskut():
    with open("laskut.csv") as file:
        right, wrong = [], []
        check = 0
        for row in file: #puretaan "laskut.csv" tiedosto
            row = row.split(";")
            if "-" in row[1]: #Jos laskukaaviossa on miinus-operandi, mennään tähän
                math = row[1].split("-")
                check = int(math[0]) - int(math[1])
                if check == int(row[2]): #Jos vastaus on oikea, mennään right-listaan
                    right.append(f"{row[0]};{row[1]};{row[2]}")
                if check != int(row[2]): #Jos vastaus on väärä, mennään wrong-listaan
                    wrong.append(f"{row[0]};{row[1]};{row[2]}")
            
            if "+" in row[1]: #Jos laskukaaviossa on plus-operandi, mennään tähän
                math = row[1].split("+")
                check = int(math[0]) + int(math[1])
                if check == int(row[2]): #Jos vastaus on oikea, mennään right-listaan
                    right.append(f"{row[0]};{row[1]};{row[2]}")

                if check != int(row[2]):#Jos vastaus on väärä, mennään wrong-listaan
                    wrong.append(f"{row[0]};{row[1]};{row[2]}")
    
    with open("oikeat.csv", "w") as file:
        for student in right:
            file.write(student)
    with open("vaarat.csv", "w") as file:
        for student in wrong:
            file.write(student)

if __name__ == "__main__":
    suodata_laskut()