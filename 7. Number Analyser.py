print("$"*30)
print("       Number Analyser")
print("$"*30)

Num = int(input("Enter a Number: "))
print("-"*30)
original_num = Num
original_num2 = Num
original_num3 = Num
original_num4 = Num

Sum = 0 #Sum Of The Digits
while Num > 0:
    digits = Num % 10
    Sum += digits
    Num //= 10
print("Sum of Digits: ", Sum)
print("-"*30)


count = 0  #Number of digits
while original_num > 0:
    count += 1
    original_num //= 10
print("Number of Digits are: ", count)
print("-"*30)

reversed_num = 0  #reversing
i = 1
while original_num2 > 0:
    Cal = original_num2 % 10
    reversed_num = (reversed_num*10) + Cal
    original_num2 //= 10
print("Reversed Number: ", reversed_num)
print("-"*30)

if reversed_num == original_num3:  #Palindrome Checking
    print("Palindrome: YES")
else:
    print("PAlindrome: NO")
print("-"*30)

j = 0
k = 0
while original_num4 > 0:
   remove = original_num4 % 10
   if remove % 2 == 0:
       j += 1
   else:
       k += 1
   original_num4 //= 10       
print("Number of Even Numbers: ", j)
print("Number of Odd Numbers: ", k)
print("-"*30)  
print("$"*30)            