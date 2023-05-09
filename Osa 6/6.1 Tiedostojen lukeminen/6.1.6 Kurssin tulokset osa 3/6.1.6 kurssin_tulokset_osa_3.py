def student_file(): #Toimii kuten pitääkin
    command = input("Opiskelijatiedot: ")
    with open(f"{command}") as file:
        for a in file:
            row = a.split(";")
            if row[0] == "opnro":
                continue
            student[row[0]] = f"{row[1]} {row[2].strip()}"

def exam_file(): #Toimii kuten pitääkin
    command = input("Koepisteet: ")
    with open(f"{command}") as file:
        for a in file:
            score = 0
            row = a.split(";")
            if row[0] == "opnro":
                continue
            for b in row[1:]:
                score += int(b)
            exam[row[0]] = score

def course_file(): #Tämä ei halua lisätä henkilöitä "Course_p" listaan, jos hänen piste on 0
    command = input("Tehtävätiedot: ")
    with open(f"{command}") as file:
        for a in file:
            score = 0
            row = a.split(";")
            a.strip()
            if row[0] == "opnro":
                continue
            for b in row[1:]:
                score += int(b)
            course[row[0]] = score
            if score >= 0 and score < 4: course_p[row[0]] = 0
            if score >= 4 and score < 8: course_p[row[0]] = 1
            if score >= 8 and score < 12: course_p[row[0]] = 2
            if score >= 12 and score < 16: course_p[row[0]] = 3
            if score >= 16 and score < 20: course_p[row[0]] = 4
            if score >= 20 and score < 24: course_p[row[0]] = 5
            if score >= 24 and score < 28: course_p[row[0]] = 6
            if score >= 28 and score < 32: course_p[row[0]] = 7
            if score >= 32 and score < 36: course_p[row[0]] = 8
            if score >= 36 and score < 40: course_p[row[0]] = 9
            if score >= 40: course_p[row[0]] = 10

def printing(): #Toimii kuten pitääkin
    n, t, tp, kp, yp, ars ="nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"
    print(f"{n:30}{t:10}{tp:10}{kp:10}{yp:10}{ars:10}")
    for student_num, name in student.items():
        if student_num in course_p and student_num in exam:
            course_exam = 0
            course_exam = course_p[student_num] + exam[student_num]
            if course_exam >= 0 and course_exam <= 14: course_exam = 0
            if course_exam >= 15.0 and course_exam <= 17.9: course_exam = 1
            if course_exam >= 18.0 and course_exam <= 20.9: course_exam = 2
            if course_exam >= 21.0 and course_exam <= 23.9: course_exam = 3
            if course_exam >= 24.0 and course_exam <= 27.9: course_exam = 4
            if course_exam >= 28.0: course_exam = 5
        print(f"{name:30}{course[student_num]:<10}{course_p[student_num]:<10}{exam[student_num]:<10}{course_p[student_num] + exam[student_num]:<10}{course_exam:<10}")

student = {}
course = {}
course_p = {}
exam = {}
student_file()
course_file()
exam_file()
printing()