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
            elif(round(grade,-1) < 40):
                outputGrades.append(grade) #33->33
            else:
                rGrade = int(round(grade,-1))
                if(rGrade < grade):
                    rGrade += 5 
                if(grade % 10 >= 5 and (rGrade - grade) >= 3):
                    outputGrades.append(grade) #67->67 
                elif(grade % 10 >= 5 and (rGrade - grade) < 3): 
                    outputGrades.append(rGrade) #38->40
                else:
                    outputGrades.append(grade) # 73->73
        print(outputGrades)