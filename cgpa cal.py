#advance level CGPA calculator
s = int(input("Enter the number of subjects :"))
CGPA = float(input("Enter the current GPA or CGPA :"))
Marks =[]
credits=[]
Total =[]
tot=0
totalcredits = 0
for j in range(1,s+1):
    creditPoints = int(input("Enter the CEDIT points in sub {}:".format(j,j+1)))
    credits.append(creditPoints)
    totalcredits += creditPoints
for i in range(1,s + 1):
    subjects = int(input("Enter the grades obtained in Subjects {}:".format(i, i + 1)))
    Marks.append(subjects)
for Marks, credits in zip(Marks, credits):
    Total.append(Marks * credits)
sum= sum(Total)
GPA = sum / totalcredits
CGPA = (CGPA + GPA) /2
print(GPA)
print(CGPA)

