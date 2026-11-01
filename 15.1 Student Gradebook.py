print("="*30)
print("         Student Gradebook")
print("="*30)

students = {
    "Varun" :  75,
    "Ananya" : 67,
    "Mayank" : 97,
    "Karthik" : 92,
    "Khushi" : 85,
    "Rahul" : 22,
    "Martin" : 39,
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
print("-"*30)

Input = input("Enter the name of the student you are searching: ")
result = students.get(Input, "Student not found!")
if result == "Student not found!":
    print(result)
else:
    print("Student Found!")
    print(Input,"got",result,"marks")
