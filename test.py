from datetime import datetime, timedelta, time
import csv

def viralliset_pisteet():
    dictionary = {}
    with open("tentin_aloitus.csv") as start_file:
        for start in csv.reader(start_file, delimiter=";"): #Puretaan "tentin_aloitus.csv" tiedosto
            with open("palautus.csv") as fin_file:
                for fin in csv.reader(fin_file, delimiter=";"): #Puretaan "palautus.csv" tiedosto
                    if start[0] in fin[0]:
                        check = aikatarkastus(start, fin)
                        if check is True: #jos aika on alle 3 tuntia, niin henkilön suoritus lisätään/päivitetään listaan
                            if fin[0] not in dictionary:
                                dictionary[fin[0]] = {}
                            elif fin[0][1] in dictionary[fin[0]] and int(fin[2]) > dictionary[fin[0]][fin[1]]:
                                dictionary[fin[0]][fin[1]] = int(fin[2]) #Jos henkilön sama kurssi on jo listalla, korkeampi numero huomioidaan ja päivitetään
                            elif fin[0][1] not in dictionary[fin[0]]:
                                dictionary[fin[0]][fin[1]] = int(fin[2]) #Jos suoritus ei ole listalla, tämä lisätään listaan
                        else:
                            #Jos False, kurssi ei huomioida ja siirrytään eteenpäin
                            continue
    print(dictionary)

def aikatarkastus(exam_start, exam_end):
    start = datetime.strptime(exam_start[1],"%H:%M")
    end = datetime.strptime(exam_end[3],"%H:%M")
    hours = end - start
    if hours > timedelta(hours=3): #Jos kurssin suorittamiseen on mennyt yli 3 tuntia, palautetaan False
        return False
    else:
        return True
        
if __name__ == "__main__":
    viralliset_pisteet()
