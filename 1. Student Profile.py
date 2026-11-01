print("Create your Student Profile")

Name = input("Enter your Name: ")
Age = int(input("Enter your Age: "))
Class = int(input("Enter your Class(Intergers only): "))
Sub = input("Which is your Fav Subject: ")
Per = float(input("Enter your percentage: "))
City = input("Where are you living(city): ")

print("="*30)
print("      STUDENT PROFILE")
print("="*30)

print("Name: ", Name)

print("Age: ", Age)

print("Class: ", Class)

print("Fav Subject: ", Sub)

if Per >= 90:
    print("Percentage: ", Per ,"[Excellent Performance!]")
elif Per >= 75:
    print("Percentage: ", Per, "[Good Job!]")
else:
    print("percentage: ", Per, "[Take it easy!]")

print("City: ", City)     