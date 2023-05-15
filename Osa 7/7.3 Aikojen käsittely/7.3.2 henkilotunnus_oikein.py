from datetime import datetime
from string import ascii_letters, digits

def onko_validi(hetu: str):
    valid, date, letter, check_mark = False, hetu[0:6]+hetu[7:10], hetu[10:11], "0123456789ABCDEFHJKLMNPRSTUVWXY"
    #Ohjelma tarkastaa, onko hetun pituus oikea
    if len(hetu) == 11:
        valid = True
    else:
        valid = False
        return valid
    #Ohjelma purkaa hetu-tunnuksen osiin
    day, month, year, marks = int(hetu[0:2]), int(hetu[2:4]), int(hetu[4:6]), hetu[6:7]
    if marks == "+": year = 1800 + year
    if marks == "-": year = 1900 + year
    if marks == "A": year = 2000 + year
    #Ohjelma tarkastaa, onko päivämäärä oikea
    try:
        birthday = datetime(year, month, day)
        valid = True
    except:
        valid = False
        return valid
    #Ohjelma tarkastaa, onko hetun tarkastusmerkki oikea
    check = int(date) % 31
    if check_mark[check] == letter:
        valid = True
        return valid
    else:
        valid = False
        return valid
    
if __name__ == "__main__":
    onko = onko_validi("230691-197H")