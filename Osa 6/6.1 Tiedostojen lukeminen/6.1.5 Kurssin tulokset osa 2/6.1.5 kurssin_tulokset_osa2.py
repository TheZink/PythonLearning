def student_file():
    command = input("Opiskelijatiedot: ")
    with open(f"{command}") as file:
        for a in file:
            row = a.split(";")
            if row[0] == "opnro":
                continue
            student[row[0]] = f"{row[1]} {row[2].strip()}"
def exam_file():
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

def course_file():
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
            if score < 4: course[row[0]] = 0
            if score >= 4 and score < 8: course[row[0]] = 1
            if score >= 8 and score < 12: course[row[0]] = 2
            if score >= 12 and score < 16: course[row[0]] = 3
            if score >= 16 and score < 20: course[row[0]] = 4
            if score >= 20 and score < 24: course[row[0]] = 5
            if score >= 24 and score < 28: course[row[0]] = 6
            if score >= 28 and score < 32: course[row[0]] = 7
            if score >= 32 and score < 36: course[row[0]] = 8
            if score >= 36 and score < 40: course[row[0]] = 9
            if score >= 40: course[row[0]] = 10
def printing():
    for student_num, name in student.items():
        if student_num in course and student_num in exam:
            course_exam = 0
            course_exam = course[student_num] + exam[student_num]
            if course_exam >= 0 and course_exam <= 14: course_exam = 0
            if course_exam >= 15.0 and course_exam <= 17.9: course_exam = 1
            if course_exam >= 18.0 and course_exam <= 20.9: course_exam = 2
            if course_exam >= 21.0 and course_exam <= 23.9: course_exam = 3
            if course_exam >= 24.0 and course_exam <= 27.9: course_exam = 4
            if course_exam >= 28.0: course_exam = 5
        print(name, course_exam)

student = {}
course = {}
exam = {}
student_file()
course_file()
exam_file()
printing()