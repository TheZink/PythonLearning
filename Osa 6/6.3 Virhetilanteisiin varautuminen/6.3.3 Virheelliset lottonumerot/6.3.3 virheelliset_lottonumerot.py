import re
def suodata_virheelliset():
    with open("lottonumerot.csv") as file, open("korjatut_numerot.csv", "w") as lottery:
        for row in file: #pilkotaan lottonumerot.csv tiedoston rivit
            lottery_list = []
            new_row = row.split()
            lottery_list.append(new_row[0])
            for column in new_row[1:]: #tässä käydään numerot kerrallaan ja muutetaan ne int-muotoon
                if "-" not in column:
                    number = re.split('[;,]', column)
                    try:
                        week = int(number[0])
                        if week >= 1 and week <= 53:
                            lottery_list.append(number[0])
                        for time in range(1, len(number)): #tässä tarkastetaan lottonumerot läpi ja tallennetaan oikeat listaan
                            try:
                                change = int(number[time])
                                if change not in lottery_list and change >= 1 and change <= 39:
                                    lottery_list.append(change)
                            except:
                                pass
                    except:
                        pass
                    if len(lottery_list) == 9:
                        lottery.write(row)
                    else:
                        continue

if __name__ == "__main__":
    suodata_virheelliset()