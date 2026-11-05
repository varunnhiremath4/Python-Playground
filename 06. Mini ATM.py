print("#"*30)
print("      MINI ATM")
print("#"*30)
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
Choose = int(input("Choose Your Option From 1/2/3/4: "))
Balance = 1000 
while Choose != 4:
    if Choose == 1:
        print("Your current balance is: ", Balance)
    elif Choose == 2:
        print("Your current balance is:", Balance)
        depo = int(input("Enter the Amount You want to Deposit: "))
        Balance += depo
        print("Deposition Successfull!")
        print("Your new balance is: ", Balance)
    elif Choose == 3:
        print("Your current balance is:", Balance)
        withdraw = int(input("Enter the Amount to be Withdrawn: "))
        if withdraw <= Balance:
            Balance -= withdraw
            print("Withdrawal Successfull!")
            print("Your New Balance is: ", Balance)
        else:
            print("Insufficient Balance!")
    if Choose not in [1, 2, 3, 4]:
        print("Invalid Operation!, Choose Again")
            
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    Choose = int(input("Choose Your Option From 1/2/3/4: "))        
if Choose == 4:
    print("Thank You!, Please Remove your Card")