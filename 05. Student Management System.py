
info = {
    "Name" : input("Enter your name: "),
    "Age" : int(input("Enter your age: ")),
    "Class" : int(input("Enter your class: ")),
    "City" : input("Enter your city: "),
    "Fav_Subject" : input("Enter your favorite subject: "),
    "Percentage" : float(input("Enter your percentage: ")),
}

print("Student Information:")
print("Name:", info["Name"])
print("Age:", info["Age"])
print("Class:", info["Class"])
print("City:", info["City"])
print("Favorite Subject:", info["Fav_Subject"])
print("Percentage:", info["Percentage"])

if info["Percentage"] >= 90:
    print("Grade: A+")
elif info["Percentage"] >= 75:
    print("Grade: B")
elif info["Percentage"] >= 60:
    print("Grade: C")
elif info["Percentage"] >= 35:
    print("Grade: D")
else:
    print("Grade: F")

if info["Percentage"] >= 95:
    print("Congratulations! You are eligible for a scholarship.")
else:
    print("You are not eligible for a scholarship.")

Updation = input("Do you want to update any information? (YES/NO): ")
if Updation == "NO":
    print("Thank you for using the Student Management System.")
elif Updation == "YES":
    Choice = input("Which Info would you like to update? (Name, Age, Class, City, Fav_Subject, Percentage): ")
    if Choice == "Name":
        info["Name"] = input("Enter your new name: ")
    elif Choice == "Age":
        info["Age"] = int(input("Enter your new age: "))
    elif Choice == "Class":
        info["Class"] = int(input("Enter your new class: "))
    elif Choice == "City":
        info["City"] = input("Enter your new city: ")
    elif Choice == "Fav_Subject":
        info["Fav_Subject"] = input("Enter your new favorite subject: ")
    elif Choice == "Percentage":
        info["Percentage"] = float(input("Enter your new percentage: "))
    else:
        print("Invalid choice.")

    print("Updated Student Information:")
    print("Name:", info["Name"])
    print("Age:", info["Age"])
    print("Class:", info["Class"])
    print("City:", info["City"])          
    print("Favorite Subject:", info["Fav_Subject"])
    print("Percentage:", info["Percentage"])
else:
    print("Invalid input. Please enter YES or NO.")