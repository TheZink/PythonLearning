def student_file():
    command = input("Opiskelijatiedot: ")
    with open(f"{command}") as file:
        for a in file:
            row = a.split(";")
            if row[0] == "opnro":
                continue
            student[row[0]] = f"{row[1]} {row[2].strip()}"
def course_file():
    command = input("Tehtävätiedot: ")
    with open(f"{command}") as file:
        for a in file:
            row = a.split(";")
            a.strip()
            if row[0] == "opnro":
                continue
            course[row[0]] = row[1:]
def printing():
    for student_num, name in student.items():
        perfomance = 0
        if student_num in course: 
            for a in course[student_num]:
                perfomance += int(a)
        print(name, perfomance)
student = {}
course = {}
student_file()
course_file()
printing()