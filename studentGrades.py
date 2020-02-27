while True:
    studentNum = int(raw_input("Enter Student Number: "))
    if(studentNum <= 0 or studentNum > 60):
        print("Student number can not be under 0 and over 60")
        break
    else: 
        grades = []
        outputGrades = []
        for i in range(studentNum):
            grades.append(raw_input("Enter Student "+str(i+1)+" Grade: "))
            grade = int(grades[i])
            if(grade < 0 or grade > 100):
                print("Grade can not be under 0 or over 100")
                break
            else:
                if(grade < 38 and grade > 80):
                    outputGrades.append(grade)
                else:
                    if(grade%10 >= 3 and grade%10 < 5):
                        temp = str(grade/10) + str(5)
                        outputGrades.append(int(temp))
                    elif(grade%10 > 5):
                        outputGrades.append(int(round(float(grade))))
                    else:
                        outputGrades.append(grade)
        print(outputGrades)