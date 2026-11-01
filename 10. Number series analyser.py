num = int(input("Enter the Number: "))
Sum = 0
even_sum = 0
odd_sum = 0
even_counter = 0
odd_counter = 0

for i in range(1, num + 1): 
    Sum += i

for j in range(2, num + 1, 2):
    even_sum += j
    even_counter += 1

for k in range(1, num + 1, 2):
    odd_sum += k
    odd_counter += 1

print("The Sum of all Numbers: ", Sum)
print("The Sum of Even Numbers: ", even_sum)
print("Number of Even Numbers: ", even_counter)
print("The Sum of Odd Numbers: ", odd_sum)
print("Number of Odd Numbers: ", odd_counter)
print("Highest Number: ", num)
print("Lowest Number: 1")