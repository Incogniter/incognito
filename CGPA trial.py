#advance level CGPA calculator
s = int(input("Enter the number of subjects :"))
l = int(input("Enter the number og lab :"))
CGPA = float(input("Enter the current GPA or CGPA :"))
library = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "RA": 0}
Marks = []
Total = []
totalcredits = []
credits =0
for j in range(1, s+1):
    subcreditPoints = int(input("Enter the CEDIT points of subject {}:".format(j, j+1)))
    totalcredits.append(subcreditPoints)
    credits += subcreditPoints
for k in range(1, l+1):
    labcreditpoints = int(input("Enter the CREDITS of lab {}:".format(k, k+1)))
    totalcredits.append(labcreditpoints)
    credits += labcreditpoints
for i in range(1, s + 1):
    subjects = input("Enter the grades obtained in Subjects {}:".format(i, i + 1))
    if subjects in library:
        answer1 = library.get(subjects)
        Marks.append(answer1)
for n in range(1, l+1):
    Lab = input("Enter the grades obtained in Lab {} :".format(n, n+1))
    if Lab in library:
        answer2 = library.get(Lab)
        Marks.append(answer2)
for Marks, totalcredits in zip(Marks, totalcredits):
    Total.append(Marks * totalcredits)
sum = sum(Total)
GPA = sum / credits
CGPA = (CGPA + GPA) / 2
print("Your GPA is ", GPA)
print("Your CGPA is ", CGPA)



#semester1 =        {"1.Communicative English -HS8151": 4,
#                 "3.Engineering Physics -PH8151 ": 3,
#                  "4.Engineering Chemistry -CY8151": 3,
#                 "5.Prob Solving & Python programming -GE8151": 3,
#                 "6.Engineering Graphics -GE8152": 4,
#                 "7.Problem Solving& Python Programming Lab -GE8161": 2,
#                 "8.Physics & Chemistry Lab -BS8161": 2}
#key_answers=[]
#num = 0
#lists= [10,10,10,10,10,10,10,10]
#semester= list(semester1)
#   key_answer =semester1.get(values)
#    for item in lists:
#        numerator = key_answer*item
#    num +=numerator
#    print(numerator)
#   print(num)