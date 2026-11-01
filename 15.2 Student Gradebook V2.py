# Note:
# - User-defined functions (def) have NOT been used.
# V3 will fix below problems:

# 1. Repeated Statistics
    # Move statistics calculation into a reusable function.

# 2. Repeated Display Code
    # Create a function to display gradebook information.

# 3. Repeated Menu
   # Create a function to display the menu.

# 4. Numbered Variables
    # Remove unnecessary sum1, sum2, sum3, etc.

# 5. Duplicate Student
    # Prevent adding a student who already exists.

# 6. Invalid Marks
   # Allow marks only within a valid range.

# 7. Invalid Menu Input
    # Handle non-numeric/invalid menu choices safely.

# 8. Invalid Marks Input
    # Handle non-numeric marks safely.

# 9. Recalculate Statistics
    # Avoid repeating the same calculation after every operation.

# 10. Cleaner Highest/Lowest Logic
     # Find a cleaner approach without repeatedly creating Items.
print("="*30) 
print("     Student Gradebook V2")
print("="*30)

students = {
    "Varun" :  25,
    "Shreya" : 67,
    "Mayank" : 97,
    "Karthik" : 53,
    "Khushi" : 42,
    "Manvith" : 75,
    "Apoorva" : 39,
}
sum1 = 0
count = 0
pass_count = 0
fail_count = 0
Items = list(students.items())
high_marks = Items[0][1]
low_marks = Items[0][1]
high_name = Items[0][0]
low_name = Items[0][0]

for name, marks in students.items():
    print("Name:",name,"-> Marks:",marks)
    sum1 += marks
    count += 1

    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

    if marks > high_marks:
        high_marks = marks
        high_name = name
    if marks < low_marks:
        low_marks = marks
        low_name = name

print("-"* 30)
print("Sum of all student's marks: ", sum1)
print("Avg of all student's marks: ", round(sum1/count, 2))
print("The number of students passed: ", pass_count)
print("The number of students failed: ", fail_count)
print("The topper of the school is",high_name,"with marks: ",high_marks)
print("The student who got least marks is",low_name,"with marks: ",low_marks)
print("="*30)
print("Operations you can perform are listed below:")
print("1. Search a Student")
print("2. Add a Student")
print("3. Update marks of a student")
print("4. Remove a Student")
print("5. Exit")
choose = int(input("Enter your option from 1/2/3/4/5: "))
print("="*30)

while choose != 5:
    if choose == 1:
        Input1 = input("Enter the name of the student you are searching: ")
        result = students.get(Input1, "Student not found!")
        if result == "Student not found!":
            print(result)
        else:
            print("Student Found!")
            print(Input1,"got",result,"marks")

    if choose == 2:
        Input_2_1 = input("Enter the name of the student you want to add: ")
        Input_2_2 = int(input("Enter his/her marks: "))
        students[Input_2_1] = Input_2_2
        Items = list(students.items())
        sum2 = 0
        count2 = 0
        pass_count2 = 0
        fail_count2 = 0
        high_marks2 = Items[0][1]
        low_marks2 = Items[0][1]
        high_name2 = Items[0][0]
        low_name2 = Items[0][0]
        print("Added Successfully!")
        print("="*30)
        print("Updated Info is below: ")
        for name2, marks2 in students.items():
            print("Name:",name2,"-> Marks:",marks2)
            sum2 += marks2
            count2 += 1

            if marks2 >= 40:
                pass_count2 += 1
            else:
                fail_count2 += 1

            if marks2 > high_marks2:
                high_marks2 = marks2
                high_name2 = name2
            if marks2 < low_marks2:
                low_marks2 = marks2
                low_name2 = name2

        print("-"* 30)
        print("Sum of all student's marks: ", sum2)
        print("Avg of all student's marks: ", round(sum2/count2, 2))
        print("The number of students passed: ", pass_count2)
        print("The number of students failed: ", fail_count2)
        print("The topper of the school is",high_name2,"with marks: ",high_marks2)
        print("The student who got least marks is",low_name2,"with marks: ",low_marks2)          
        
    if choose == 3: 
        Input_3_1 = input("Enter the existing student name: ")
        if Input_3_1 in students:
            Input_3_2 = int(input("Enter the Updated Marks of the student: "))
            students[Input_3_1] = Input_3_2
            Items = list(students.items())
            sum3 = 0
            count3 = 0
            pass_count3 = 0
            fail_count3 = 0
            high_marks3 = Items[0][1]
            low_marks3 = Items[0][1]
            high_name3 = Items[0][0]
            low_name3 = Items[0][0]
            print("Updated Successfully!")
            print("="*30)
            print("Updated Info is below: ")
            for name3, marks3 in students.items():
                print("Name:",name3,"-> Marks:",marks3)
                sum3 += marks3
                count3 += 1

                if marks3 >= 40:
                    pass_count3 += 1
                else:
                    fail_count3 += 1

                if marks3 > high_marks3:
                    high_marks3 = marks3
                    high_name3 = name3
                if marks3 < low_marks3:
                    low_marks3 = marks3
                    low_name3 = name3

            print("-"* 30)
            print("Sum of all student's marks: ", sum3)
            print("Avg of all student's marks: ", round(sum3/count3, 2))
            print("The number of students passed: ", pass_count3)
            print("The number of students failed: ", fail_count3)
            print("The topper of the school is",high_name3,"with marks: ",high_marks3)
            print("The student who got least marks is",low_name3,"with marks: ",low_marks3) 
        else:
            print(Input_3_1,"does not exist!")
            print("Add him first by choosing 2 in menu!")

    if choose == 4:  
        Input_4 = input("Enter the existing student's name you want delete: ")
        if Input_4 in students:
            del students[Input_4]
            Items = list(students.items())
            sum4 = 0
            count4 = 0
            pass_count4 = 0
            fail_count4 = 0
            high_marks4 = Items[0][1]
            low_marks4 = Items[0][1]
            high_name4 = Items[0][0]
            low_name4 = Items[0][0]
            print("Deleted successfully!")
            print("="*30)
            print("Updated Info is below: ")
            for name4, marks4 in students.items():
                print("Name:",name4,"-> Marks:",marks4)

                sum4 += marks4
                count4 += 1

                if marks4 >= 40:
                    pass_count4 += 1
                else:
                    fail_count4 += 1

                if marks4 > high_marks4:
                    high_marks4 = marks4
                    high_name4 = name4
                if marks4 < low_marks4:
                    low_marks4 = marks4
                    low_name4 = name4

            print("-"* 30)
            print("Sum of all student's marks: ", sum4)
            print("Avg of all student's marks: ", round(sum4/count4, 2))
            print("The number of students passed: ", pass_count4)
            print("The number of students failed: ", fail_count4)
            print("The topper of the school is",high_name4,"with marks: ",high_marks4)
            print("The student who got least marks is",low_name4,"with marks: ",low_marks4)

        else:
            print(Input_4,"does not exist!")
            print("Add him first by choosing 2 in menu!") 
        
    print("="*30)
    print("Operations you can perform are listed below:")
    print("1. Search a Student")
    print("2. Add a Student")
    print("3. Update marks of a student")
    print("4. Remove a Student")
    print("5. Exit")
    choose = int(input("enter your option from 1/2/3/4/5: "))
    print("="*30)

if choose == 5:
    print("Exited the menu successfully!")