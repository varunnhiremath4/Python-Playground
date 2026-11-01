print("="*43)
print(" Welcome to Smart Student Result Validator")
print("="*43)
class MarksError(Exception):
    pass 
try:
    name = input("Enter your Name: ")
    M_cs = int(input("Enter your Cs Marks: "))
    M_maths = int(input("Enter your Maths Marks: "))
    M_p = int(input("Enter your Physics Marks: "))
    if M_cs>100 or M_maths>100 or M_p>100 or M_p<0 or M_maths<0 or M_cs<0:
        raise MarksError("Marks should be b/w 0 to 100")
    print("-"*30)
    M_avg = (M_cs + M_maths + M_p) / 3
except MarksError as r:
    print(r)
    print("-"*30)
except ValueError:
    print("Marks should be integer")
    print("-"*30)
else:
    print("Avg marks: ", round(M_avg, 2))
    print("Result Validated successfully")
    print("-"*30)
finally:
    print("Thanks for using Validator")

