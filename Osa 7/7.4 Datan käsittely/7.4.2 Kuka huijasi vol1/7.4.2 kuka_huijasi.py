from datetime import datetime, timedelta, time
import csv

def huijarit():
    cheater, amount = [], 0
    with open("tentin_aloitus.csv") as start_file:
        for exam_start in csv.reader(start_file, delimiter=";"):
            with open("palautus.csv") as return_file:
                for exam_end in csv.reader(return_file, delimiter=";"):
                    if exam_start[0] in exam_end[0]:
                        a = datetime.strptime(exam_start[1],"%H:%M")
                        b = datetime.strptime(exam_end[3],"%H:%M")
                        c = b - a
                        if c > timedelta(hours=3):
                            amount += 1
                            if exam_end[0] not in cheater:
                                cheater.append(exam_end[0])
    return cheater
if __name__ == "__main__":
    huijarit()