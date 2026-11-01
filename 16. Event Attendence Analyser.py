print("="*40)
print("       Event Attendance Analyzer")
print("="*40)

python_students = {
    "Varun", "Ananya", "Rahul", "Karthik",
    "Khushi", "Mayank", "Riya"
}

web_students = {
    "Ananya", "Karthik", "Mayank", "Arjun",
    "Riya", "Sneha", "Rahul"
}

ai_students = {
    "Varun", "Karthik", "Arjun", "Sneha",
    "Mayank", "Priya", "Rahul"
}

all_three = python_students & web_students & ai_students

python_web_students = python_students & web_students - ai_students

atleast_one = python_students | web_students | ai_students

atleast_one_count = 0
for i in atleast_one:
    atleast_one_count += 1

python_only = python_students - web_students - ai_students
web_only = web_students - python_students - ai_students
ai_only = ai_students - web_students - python_students
exactly_one = python_only | web_only | ai_only

print("-"*100)
print("Python Students:", python_students)
print("-"*100)
print("Web Students:", web_students)
print("-"*100)
print("AI Students:", ai_students)
print("-"*100)
print("The students who are present in all three events are: ", all_three)
print("-"*100)
print("The students who attended Python and web but not in Ai: ", python_web_students)
print("-"*100)
print("Students attended atleast one: ", atleast_one)
print("Count of students who have attended atleast one: ", atleast_one_count)
print("-"*100)
print("Students who have attended exactly one event: ", exactly_one)
print("="*100)
user_input = input("The name of the student you want to check: ")
print("The event you want to check for: ")
print("1. Python")
print("2. Web")
print("3. AI")
print("4. Exit")
choose = int(input("Enter your choice 1/2/3/4: "))


while choose != 4:
    if choose == 1:
        if user_input in python_students:
            print(user_input, "attended the Python event!")
        else:
            print(user_input, "didn't attend the Python event!")
    if choose == 2:
        if user_input in web_students:
            print(user_input, "attended the Web event!")
        else:
            print(user_input, "didn't attend the Web event!")
    if choose == 3:
        if user_input in ai_students:
            print(user_input, "attended the AI event!")
        else:
            print(user_input, "didn't attend the AI event!")
    print("="*100)
    user_input = input("The name of the student you want to check: ")
    print("The event you want to check for: ")
    print("1. Python")
    print("2. Web")
    print("3. AI")
    print("4. Exit")
    choose = int(input("Enter your choice 1/2/3/4: "))
    

if choose == 4:
    print("Quitted the menu!")