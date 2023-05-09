def main():
    student = input("opiskelijatiedot: ")
    assignments = input("tehtävätiedot: ")
    exam = input("koepisteet: ")
    course = input("kurssin tiedot: ")
    a = student_file(student)
    b = assignments_file(assignments)
    c = exam_file(exam)
    d = course_file(course)
    printing(a, b, c, d)

def student_file(student): #Funktio purkaa opiskelijatiedot ja tallentaa ne dict-listaan
    student_data = {}
    with open(student) as file:
        for row in file:
            row = row.split(";")
            if row[0] == "opnro":
                continue
            student_data[row[0]] = f"{row[1]} {row[2].strip()}"
    return student_data

def assignments_file(assignments): #Funktio purkaa tehtävätiedot ja tallentaa ne dict-listaan
    assignments_data = {}
    with open(assignments) as file:
        for row in file:
            score = 0
            row = row.split(";")
            if row[0] == "opnro":
                continue
            for exam_score in row[1:]:
                score += int(exam_score)
            assignments_data[row[0]] = score
    return assignments_data

def exam_file(exam): #Funktio purkaa ja laskee koepisteet yhteen ja tallentaa ne dict-listaan
    exam_data = {}
    with open(exam) as file:
        for row in file:
            scores = 0
            row = row.split(";")
            if row[0] == "opnro":
                continue
            for score in row[1:]:
                scores += int(score)
            exam_data[row[0]] = scores
    return exam_data

def course_file(course): #Funktio purkaa kurssin tiedot ja tallentaa ne listaan
    course_list = []
    with open(course) as file:
        for name in file:
            cut = name.split(": ")
            course_list.append(cut[1].strip())
    return course_list

def printing(student: dict, assigment: dict, exam: dict, course: list): #Funktio purkaa yllä olevat listat ja laskee pisteet yhteen sekä antaa arvosanan.
    score_list = {}
    course_name = f"{course[0]}, {course[1]} opintopistettä"
    with open("tulos.txt", "w") as file: #Tiedot tallennetaan tekstitiedostona
        file.write(f"{course_name}\n")
        file.write(f"{'='*len(course_name)}\n")
        file.write(f"{'nimi':30}{'teht_lkm':10}{'teht_pist':10}{'koe_pist':10}{'yht_pist':10}{'arvosana':10}\n")
        for student_number, name in student.items():
            if student_number in assigment and student_number in exam:
                grade = 0
                course_score = assigment[student_number] // 4 + exam[student_number]
                if course_score >= 0 and course_score <= 14: grade = 0
                if course_score >= 15.0 and course_score <= 17.9: grade= 1
                if course_score >= 18.0 and course_score <= 20.9: grade = 2
                if course_score >= 21.0 and course_score <= 23.9: grade = 3
                if course_score >= 24.0 and course_score <= 27.9: grade = 4
                if course_score >= 28.0: grade = 5
            file.write(f"{name:30}{assigment[student_number]:<10}{assigment[student_number]//4:<10}{exam[student_number]:<10}{course_score:<10}{grade:<10}\n")
            score_list[student_number] = name, grade 
    with open("tulos.csv", "w") as file: #Tiedot tallennetaan csv-tiedostona
        for student_number in score_list:
            file.write(f"{student_number};{score_list[student_number][0]};{score_list[student_number][1]}\n")
main()