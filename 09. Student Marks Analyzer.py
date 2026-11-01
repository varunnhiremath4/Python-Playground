print("="*30)
print("    Student Marks Analyser")
print("="*30)

# Taking the input of Number of subjects
Sub = int(input("Enter the number of subjects?: "))

Sum = 0
pass_count = 0     #Some Imp Variables
fail_count = 0
print("-"*30)
# Main Loop
for i in range(1, Sub+1):
    # For Entering Each Marks
    j = int(input("Enter the marks of subject " + str(i) + ":")) 
    Sum += j # Adding

    if j >= 40:      # Calculating Number of pass and fail Counts
        pass_count += 1
    else:
        fail_count += 1
    
    if i == 1:       #Calculating highest and lowest marks
        higher = j
        lower = j
    if j > higher:
        higher = j
    elif j < lower:
        lower = j
print("~"*30)  
print("Total marks you obtained: ",Sum)
print("Your average is: ", Sum/Sub)
print("The number of exams you Passed: ", pass_count)
print("The number of exams you Failed: ", fail_count)
print("The highest you obtained is: ", higher)
print("The lowest marks you obtained is: ", lower)
if fail_count >= 1:   #Printing Overall Result
    print("Overall Result: Fail")
else:
    print("Overall Result: Pass")
print("~"*30)