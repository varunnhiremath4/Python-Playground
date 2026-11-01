print("="*30)
print("Welcome to Smart Calculator V2👌")
print("="*30)
print("1. Addition➕")
print("2. Subtraction➖")
print("3. Multiplication✖️")
print("4. Division➗")
print("Enter 'q' to quit😔")
print("-"*30)
opt_input = input("Enter your option😀: ")
while opt_input != 'q':
        try:
            if opt_input == '1':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result: ", num1 + num2)
            elif opt_input == '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result: ", num1 - num2)
            elif opt_input == '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result: ", num1 * num2)
            elif opt_input == '4':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if num2 == 0:
                    raise ZeroDivisionError("Denominator cannot be zero💀")
                print("Result: ", num1 / num2)
            else:
                print("Invalid option! Please try again.")
        except ValueError:
            print("Invalid input! Please enter numeric values only.💀")
        except ZeroDivisionError as e:
            print(e)
        else:
            print("what's next you wanna try?😊")
        print("="*30)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("Enter 'q' to quit")
        opt_input = input("Enter your option: ")
if opt_input == 'q':
    print("Thanks for using Smart Calculator V2! Goodbye!")