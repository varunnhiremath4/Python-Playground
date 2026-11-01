print("-"*30)
print("Creating your Report Card")
print("-"*30)

Name = input("Enter your Name: ")
english_marks = float(input("Enter your English marks: "))
maths_marks = float(input("Enter your Maths marks: "))
science_marks = float(input("Enter your Science marks: "))

total_marks = english_marks + maths_marks + science_marks
percentage = (total_marks / 300) * 100

print("="*30)
print("      REPORT CARD")
print("="*30)
print("Name: ", Name)
print("English Marks: ", english_marks)
print("Maths Marks: ", maths_marks)
print("Science Marks: ", science_marks)
print("-"*30) 
print("Total Marks: ", total_marks)
print("Percentage: ", percentage)


if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 35: 
    print("Grade: D") 
else:
    print("Grade: F")

if percentage >= 90:
    print("Remark: Outstanding Performance!")
elif percentage >= 75:
    print("Remark: Good Job!")
elif percentage >= 60:
    print("Remark: Average Performance!")
elif percentage >= 35:
    print("Remark: Need Improvement!")
else:
    print("Don't worry, You will Succeed in Life One Day!")

if english_marks < 35 or maths_marks < 35 or science_marks < 35:
    print("Result: Fail")
else:
    print("Result: Pass")