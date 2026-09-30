students={}   #empty dictionary in which date would be stored 
while True:
    print("\n"+" Student Evaluation System ".center(50, "*"))
    print("1.Add a student")
    print("2.Add marks for 4 subjects")
    print("3.Reports")
    print("4.View all students")
    print("5.Exit The Sysyem")
    choice=input("Enter a response: ").strip()      #strip() function removes all leading and trailing whitespace (spaces, tabs \t, and newlines \n) from a string
    if choice=="1":
        student=input("Enter the student's name: ").strip()
        if student=="":
            print("Name cannot be empty.")
        elif student in students:
            print("That student is already in the database.")
        else:
            students[student]=[]
            print(student,"added.")
    elif choice=="2":
        if len(students)==0:
            print("The database is empty.Please add a student first.")
        else:
            student=input("Enter the student's name: ").strip()
            if student not in students:
                print("Student not found.")
            else:
                new_marks=[]
                valid_marks=True
                for subject in range(1, 5):
                    mark_text=input(
                        "Enter whole-number marks for subject "
                        + str(subject) + ": "
                    ).strip()
                    if not mark_text.isdigit():
                        print("Please enter a whole number.")
                        valid_marks=False
                        break
                    mark=int(mark_text)
                    if mark<0 or mark>100:
                        print("Marks must be between 0 and 100.")
                        valid_marks=False
                        break       #breakin the loop
                    new_marks.append(mark)
                if valid_marks:
                    students[student]=new_marks
                    print("Marks added for",student + ".")
    elif choice=="3":
        print("\n---Reports---")
        print("1.Overall average of all students")
        print("2.Average and CGPA of all students")
        print("3.Average and CGPA of one student")
        report_choice=input("Choose a report: ").strip()
        if report_choice=="1":
            total_marks=0
            number_of_marks=0
            for student in students:
                for mark in students[student]:
                    total_marks=total_marks+mark
                    number_of_marks = number_of_marks+1
            if number_of_marks==0:
                print("No marks have been entered yet.")
            else:
                average=total_marks/number_of_marks
                print("Overall average:",round(average,2))
        elif report_choice=="2":
            if len(students)==0:
                print("No students have been added yet.")
            else:
                for student in students:
                    if len(students[student])==0:
                        print("No marks entered for",student)
                    else:
                        total_marks=0
                        for mark in students[student]:
                            total_marks=total_marks+mark
                        average=total_marks/4
                        cgpa=average/10
                        print(student,"average:",round(average,2))
                        print(student,"CGPA:",round(cgpa,2))
        elif report_choice=="3":
            student=input("Enter the student's name: ").strip()
            if student not in students:
                print("Student not found.")
            elif len(students[student])!=4:
                print("Enter all 4 subject marks for", student, "first.")
            else:
                total_marks=0
                for mark in students[student]:
                    total_marks=total_marks+mark
                average=total_marks/4
                cgpa=average/10
                print(student,"average:",round(average,2))
                print(student,"CGPA:",round(cgpa,2))
        else:
            print("Please choose a report from 1 to 3.")
    elif choice=="4":
        if len(students)==0:
            print("No students have been added yet.")
        else:
            for student in students:
                print(student)
    elif choice=="5":
        print("Thanks for using the system.")
        break
    else:
        print("Please choose a number from 1 to 5.")
