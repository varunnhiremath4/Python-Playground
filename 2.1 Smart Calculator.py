Num1 = float(input("Enter your 1st number: "))
Num2 = float(input("Enter your 2nd number: "))
print("="*30)
print("Choose your operation: ")
print("="*30)
print("1. Addition")    
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("-"*30)
Operation = input("Enter your choice (1/2/3/4): ")
print("-"*30)
if Operation == "1":
    print("The result of Addition is: ", Num1 + Num2)
elif Operation == "2":
    print("The result of Subtraction is: ", Num1 - Num2)
elif Operation == "3":
    print("The result of Multiplication is: ", Num1 * Num2)
elif Operation == "4":
    if Num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result of Division is: ", Num1 / Num2)
elif Operation not in ["1", "2", "3", "4"]:
    print("Error: Invalid operation choice.")