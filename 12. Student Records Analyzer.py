students = [
    ("Ananya", 17, 95),
    ("Varun", 16, 100),
    ("khushi", 15, 99),
    ("Mayank", 17, 90),
    ("Karthik", 16, 82),
    ("Rahul", 18, 37),
] 
highest = students[0][2]
lowest = students[0][2]
highest_Name = str
Lowest_Name = str
Sum = 0
Count = 0
pass_count = 0
fail_count = 0


for i in students:
    Name, age, Marks = i
    print("Name:",Name, " Age:",age, " Marks:", Marks)
    
    
    Sum += Marks
    Count += 1


    if Marks > highest:
        highest = Marks
        highest_Name = Name
    if Marks < lowest:
        lowest = Marks
        Lowest_Name = Name

    if Marks >= 40:
        pass_count += 1
    if Marks < 40:
        fail_count += 1


print("The student who got the Highest marks is: ", highest_Name, ": ", highest)
print("The student who got the Lowest marks is: ", Lowest_Name, ": ", lowest)
print("Sum of Marks of All Students: ", Sum)
print("Average Marks of All students: ", Sum/Count)
print("Number of Students passed: ", pass_count)
print("Number of Students failed: ", fail_count)
Input_Name = input("Enter the name you want to know about: ")

found = False

for j in students:
    Name, age, Marks = j 
   
    if Name == Input_Name:
        print(j)
        found = True

if found == True:
    None
elif found == False:
    print("No search results!")