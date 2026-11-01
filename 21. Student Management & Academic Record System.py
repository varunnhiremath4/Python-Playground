print("="*44)
print("Student Management & Academic Record System")
print("="*44)
students = []
student_1 = {
    "Name": "Varun",
    "Age": 20,
    "Subjects": ["Math", "Computer Science", "Physics"],
    "Marks" : {
        "Math": 85,
        "Computer Science": 90,
        "Physics": 78
    }
}
student_2 = {
    "Name": "Mayank",
    "Age": 21,
    "Subjects": ["Math", "Computer Science", "Chemistry"],
    "Marks" : {
        "Math": 88,
        "Computer Science": 92,
        "Chemistry": 80
    }
}
student_3 = {
    "Name": "Apoorva",
    "Age": 19,
    "Subjects": ["Math", "Biology", "Chemistry"],
    "Marks" : {
        "Math": 90,
        "Biology": 85,
        "Chemistry": 88
    }
}
students.append(student_1)
students.append(student_2)
students.append(student_3)
count = 0
for i in students:
    count += 1
    print("Student",count,": ", i["Name"])
print("-"*47)
print("Now Displaying the Academic Record of Students")
print("-"*47)
for i in students:
    print("Name: ", i["Name"])
    print("Age: ", i["Age"])
    print("Subjects: ", i["Subjects"])
    for subject, marks in i["Marks"].items():
        print(subject, ":", marks)
    print("-"*47)
print("Student seaching and record retrieval is now available.")
s_input = input("Enter S to continue or s to skip this feature: ")
while s_input == "S":
    search_name = input("Enter the name of the student to search: ")
    found = False
    for i in students:
        if i["Name"].lower() == search_name.lower():
            found = True
            print("-"*47)
            print("Student found. Displaying the academic record:")
            print("Name: ", i["Name"])
            print("Age: ", i["Age"])
            print("Subjects: ", i["Subjects"])
            for subject, marks in i["Marks"].items():
                print(subject, ":", marks)
            print("-"*47)
            break
    if found == False:
        print("Student not found.")
    s_input = input("Enter S to continue or s to skip this feature: ")
print("-"*47)
print("Student Update and record modification is now available.")
u_input = input("Enter U to continue or u to skip this feature: ")
while u_input == "U":
    update_name = input("Enter the name of the student to update: ")
    found = False
    for i in students:
        if i["Name"].lower() == update_name.lower():
            found = True
            print("-"*47)
            print("Student found. You can now update the academic record:")
            print("Which one do you want to update?")
            print("1. Age")
            print("2. Marks")
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1":
                new_age = int(input("Enter the new age: "))
                i["Age"] = new_age
                print("Age updated successfully.")
            elif choice == "2":
                subject_to_update = input("Enter the subject to update marks for: ")
                if subject_to_update in i["Marks"]:
                    new_marks = int(input("Enter the new marks: "))
                    i["Marks"][subject_to_update] = new_marks
                    print("Marks updated successfully.")
                else:
                    print("Subject not found.")
            break
    if found == False:
        print("Student not found.")
    another_update = input("Do you wanna use this feature again? (Y/N): ")
    if another_update.lower() == "n":
        break
    elif another_update.lower() == "y":
        u_input = "U"
    else:
        print("Invalid input. Exiting update feature.")
        break

print("-"*47)
print("Student Deletion and record removal is now available.")
d_input = input("Enter D to continue or d to skip this feature: ")
while d_input == "D":
    delete_name = input("Enter the name of the student to delete: ")
    found = False
    for i in students:
        if i["Name"].lower() == delete_name.lower():
            found = True
            students.remove(i)
            print("Student record deleted successfully.")
            break
    if found == False:
        print("Student not found.")
    another_delete = input("Do you wanna use this feature again? (Y/N): ")
    if another_delete.lower() == "n":
        break
    elif another_delete.lower() == "y":
        d_input = "D"
    else:
        print("Invalid input. Exiting deletion feature.")
        break
print("-"*47)
print("Addition of new student records is now available.")
a_input = input("Enter A to continue or a to skip this feature: ")
while a_input == "A":
    print("Please enter the details of the new student:")
    found = False
    new_student_name = input("Enter the name of the student: ")
    for student in students:
        if new_student_name.lower() == student["Name"].lower():
            print("Student already exists.")
            found = True
            break
    if found == False:
        new_student_age = int(input("Enter the age of the student: "))
        new_student_subjects1 = input("Enter the first subject: ")
        new_student_subjects2 = input("Enter the second subject: ")
        new_student_subjects3 = input("Enter the third subject: ")
        new_student_subjects = [new_student_subjects1, new_student_subjects2, new_student_subjects3]
        new_student_marks = {}
        for subject in new_student_subjects:
            marks = int(input("Enter the marks for " + subject + ": "))
            new_student_marks[subject] = marks
        new_student = {
            "Name": new_student_name,
            "Age": new_student_age,
            "Subjects": new_student_subjects,
            "Marks": new_student_marks
        }
        students.append(new_student)
        print("New student record added successfully.")
    another_add = input("Do you wanna use this feature again? (Y/N): ")
    if another_add.lower() == "n":
        break
    elif another_add.lower() == "y":
        a_input = "A"
    else:
        print("Invalid input. Exiting addition feature.")
        break
print("-"*47)
print("View record feature is now available.")
c_input = input("Enter C to continue or c to skip this feature: ")
while c_input == "C":
    cal_name = input("Name of the student whose records to be calculated: ")
    found = False
    for student in students:
        if cal_name.lower() == student["Name"].lower():
            found = True
            print("Here are the records of this student")
            cal_marks = 0 
            count = 0
            for sub, marks in student["Marks"].items():
                cal_marks += marks
                count += 1
            print("Total marks obtained: ", cal_marks)
            print("Average Marks obtained: ", round(cal_marks/count, 2))
            print("Scored percent: ", round((cal_marks/300)*100, 2))
            if cal_marks >= 250:
                Grade = "A"
            elif cal_marks >= 200:
                Grade = "B"
            elif cal_marks >= 150:
                Grade = "C"
            elif cal_marks >= 100:
                Grade = "D"
            elif cal_marks >= 50:
                Grade = "E"
            else:
                Grade = "F"
            print("Overall Grade: ", Grade)
    if found == False:
        print("Student Not Found")
    another_input = input("Do wanna use this feature again?[Y/N]: ")
    if another_input.lower() == "n":
        break
    elif another_input.lower() == "y":
        c_input ="C"
    else:
        print("Invalid input. Exiting view record feature.")
        break