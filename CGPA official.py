grade_points = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "RA": 0}
semester1 = {"1.Communicative English -HS8151": 4,
             "2.Mathematics I -MA8151": 4,
             "3.Engineering Physics -PH8151 ": 3,
             "4.Engineering Chemistry -CY8151": 3,
             "5.Prob Solving & Python programming -GE8151": 3,
             "6.Engineering Graphics -GE8152": 4,
             "7.Problem Solving& Python Programming Lab -GE8161": 2,
             "8.Physics & Chemistry Lab -BS8161": 2}
semester2 = {"1.Technical English - HS8251": 4,
             "2.Mathematics II - MA8251": 4,
             "3.Materials Science - PH8251": 3,
             "4.Basic Electrical, Electronics & Instr Engi - BE8253": 3,
             "5.Environmental Science & Engineering - GE8291": 3,
             "6.Engineering Mechanics - GE8292": 4,
             "7.Basic Electrical, Electronics & Instr Engi - BE8261": 2,
             "8.Engineering Practices Lab - GE8261": 2}
semester3 = {"1.Transforms and Partial Differential Equations - MA8353": 4,
             "2.Engineering Thermodynamics - ME8391": 4,
             "3.Fluid Mechanics and Machinery - CE8394": 4,
             "4.Manufacturing Technology I - ME8351": 3,
             "5.Electrical Drives and Controls - EE8353": 3,
             "6.Manufacturing Technology Lab - ME8361": 2,
             "7.Computer Aided Machine Drawing - ME8381": 2,
             "8.Electrical Engineering Lab - EE8361": 2,
             "9.Interpersonal Skills / Listening & Speaking - HS8381": 1}
semester4 = {"1 Statistics and Numerical Methods - MA8452": 4,
             "2.Kinematics of Machinery - ME8492": 3,
             "3.Manufacturing Technology II - ME8451": 3,
             "4.Engineering Metallurgy - ME8491": 3,
             "5.Strength of Materials for Mechanical Engineers - CE8395": 3,
             "6.Thermal Engineering- I - ME8493": 3,
             "7.Manufacturing Technology LabII - ME8462": 2,
             "8.Strength of Materials & fluid MM Lab - CE8381": 2,
             "9.Advanced Reading and Writing - HS8461": 1}
semester5 = {"1.Thermal Engineering- II -ME8595": 3,
             "2.Design of Machine Elements -ME8593": 3,
             "3.Metrology and Measurements -ME8511": 3,
             "4.Dynamics of Machines -ME8594": 3,
             "5.Open Elective I -": 3,
             "6.Kinematics and Dynamics Lab -": 2,
             "7.Thermal Engineering Lab -ME8512": 2,
             "8.Metrology and Measurements Lab -ME8513": 2}
semester6 = {"1 Design of Transmission Systems -ME8651": 3,
             "2.Computer Aided Design & Manufacturing -ME8691": 3,
             "3.Heat and Mass Transfer -ME8693": 4,
             "4.Finite Element Analysis -ME8692": 3,
             "5.Hydraulics and Pneumatics -ME8694": 3,
             "6.Professional Elective I -": 3,
             "7.CAD CAM LAb -ME8681": 2,
             "8.Design & Fabrication Project -ME8682": 2,
             "9.Professional Communication -HS8581": 1}
semester7 = {"1 Power Plant Engineering - ME8792": 3,
             "2.Process Planning and Cost Estimation - ME8793": 3,
             "3.Mechatronics - ME8791": 3,
             "4.Open Elective - II -": 3,
             "5.Professional Elective II -": 3,
             "6.Professional Elective III -": 3,
             "7.Simulation & Analysis LAb - ME8711": 2,
             "8.Mechatronics Lab - ME8781": 2,
             "9.Technical Seminar - ME8712": 1}
semester8 = {"1 Principles of Management - MG8591": 3,
             "2.Professional Elective– IV": 3,
             "3.Project Work -": 10}


mechanical = {1: semester1,
              2: semester2,
              3: semester3,
              4: semester4,
              5: semester5,
              6: semester6,
              7: semester7,
              8: semester8}
grade_point = []
TotalCredits = 0
numerator = 0
sem = int(input("Enter the semester to calculate: "))
PCGPA = float(input("Enter you previous CGPA: "))
if sem in mechanical:
    semester = mechanical.get(sem)
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
            CGPA = (PCGPA + GPA) / 2
    print("Your GPA is: ", GPA)
    print("your CGPA is: ", CGPA)







