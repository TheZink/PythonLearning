from datetime import datetime, timedelta, time
import csv

def viralliset_pisteet():
    dictionary = {}
    with open("tentin_aloitus.csv") as start_file:
        for start in csv.reader(start_file, delimiter=";"):
            with open("palautus.csv") as fin_file:
                for fin in csv.reader(fin_file, delimiter=";"):
                    if start[0] in fin[0]: #Jos henkilö palautti tentin, tarkastetaan aika
                        check = timecheck(start, fin)
                        if check is True: #jos aika on alle 3 tuntia, suoritus lisätään/päivitetään listaan
                            if fin[0] not in dictionary:
                                dictionary[fin[0]] = {}
                            if fin[1] in dictionary[fin[0]]:
                                if int(fin[2]) > dictionary[fin[0]][fin[1]]:
                                    dictionary[fin[0]][fin[1]] = int(fin[2])
                            elif fin[1] not in dictionary[fin[0]]:
                                dictionary[fin[0]][fin[1]] = int(fin[2])
                        else:
                            #Jos False, kurssi ei huomioida ja siirrytään eteenpäin
                            continue
    student_score = scoring(dictionary)
    return student_score

def timecheck(exam_start, exam_end):
    start = datetime.strptime(exam_start[1],"%H:%M")
    end = datetime.strptime(exam_end[3],"%H:%M")
    hours = end - start
    if hours > timedelta(hours=3): #Jos kurssin suorittamiseen on mennyt yli 3 tuntia, palautetaan False
        return False
    else:
        return True

def scoring(dictionary):
    student_score = {}
    for student, course in dictionary.items():
        scores = 0
        for key, value in course.items():
            scores += value
        student_score[student] = scores
    return student_score

if __name__ == "__main__":
    viralliset_pisteet()
