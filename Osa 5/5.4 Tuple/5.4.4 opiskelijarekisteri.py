def lisaa_opiskelija(stud_list: list, student: str): #Funktio lisää opiskelijan sanakirjaan
    if student not in stud_list:
        stud_list[student] = ""
    return stud_list

def tulosta(stud_list: list, student: str): #Funktio tulostaa opiskelijan tiedot
    for name, perfomance in stud_list.items(): #Funktio purkaa "opiskelijat"-sanakirjan
        if student == name:
            print(f"{name}:")
            if perfomance == "":
                print(" ei suorituksia")
            else:
                average = 0
                incomplete = 0
                course = {}
                for a, b in perfomance: #Funktio purkaa sanakirjassa olevan listan
                    if a not in course and b > 0:
                        course[a] = b
                        average += b
                    if a in course and b > course[a]:
                        average -= course[a]
                        course[a] = b
                        average += b
                    if b == 0:
                        incomplete += 1
                if incomplete == len(perfomance):
                    print(" ei suorituksia")
                else:
                    print(f" suorituksia {len(course)} kurssilta:")
                    for result, score in course.items(): #Funktio purkaa "Course"-sanakirjan ja printtaa niitä
                        print(f"  {result} {score}")
                    print(f" keskiarvo {average / len(course):.1f}") 
    if student not in stud_list:
        print(f"ei löytynyt ketään nimellä {student}")

def lisaa_suoritus(stud_list: list, student: str, course: tuple): #Funktio lisää opiskelijalle kurssisuorituksen
    if student in stud_list:
       if stud_list[student] == "":
           stud_list[student] = [course]
       else:
           stud_list[student].append(course)

def kooste(opiskelijat: list):
    perfomance = 0
    name_perf = ""
    name_avg = ""
    score_avg = 0
    for name, course in opiskelijat.items(): #Funktio purkaa "opiskelijat"-sanakirjan
        check = {}
        avg = 0
        for a, b in course: #Funktio purkaa listassa olevan tuplen
            if a in check: #Funktio tarkastaa, onko tuplessa oleva avain olemassa "check"-sanakirjassa
                for c,d in check.items():
                    if a == c and b > int(d):
                        avg = avg - int(d)
                        check[a] = f"{b}"
                        avg = avg + b
            if a not in check and b > 0:
                check[a] = f"{b}"
                avg = avg + b
            if len(check) > perfomance:
                perfomance = len(check)
                name_perf = name
        if avg / len(check) > score_avg:
            score_avg = avg / len(check)
            name_avg = name
        check.clear()
    print("opiskelijoita", len(opiskelijat))
    print("eniten suorituksia", perfomance, name_perf)
    print("paras keskiarvo", score_avg, name_avg)        

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "emilia")
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
    lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
    lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
    kooste(opiskelijat)