from Library import department
from Library import dep
from Library import grade_points
for val in dep:
    print(val)
grade_point = []
TotalCredits = 0
numerator = 0
num = 0
n = int(input("Enter your department: "))
depart = department.get(n)
sem = int(input("Enter the semester to calculate: "))
if sem != 1:
    PCGPA = float(input("Enter you previous CGPA: "))
if sem in depart:
    semester = depart.get(sem)
    SEMESTER = list(semester)
    for values in SEMESTER:
        grades = input(values + " : ")
        key_answer = semester.get(values)
        TotalCredits += key_answer
        if grades in grade_points:
            grade = grade_points.get(grades)
            grade_point.append(grade)
            for item in grade_point:
                num = key_answer * item
            numerator += num
    GPA = numerator/TotalCredits
    if sem == 1:
        CGPA = GPA
    else:
        CGPA = (PCGPA + GPA) / 2
    print("Your GPA is: ", GPA)
    print("your CGPA is: ", CGPA)