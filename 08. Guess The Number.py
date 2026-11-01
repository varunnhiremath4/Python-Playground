print("-"*30)
print("      Guess The Number!")
print("_"*30)

sec_num = 69
print("You have 8 attempts to guess the number, Be Quick!")
n = int(input("Guess the Number Between 1-100: "))

count = 0
attempt = 1

while 1 <= n <= 100 and attempt < 8:
    count += 1
           
    if n > sec_num:
        print("Choose Lower!")
        n = int(input("Guess the Number Between 1-100: "))
        attempt += 1
    elif n < sec_num:
        print("Choose Higher!")
        n = int(input("Guess the Number Between 1-100: "))
        attempt += 1
    elif n == sec_num:
        print("Hurray! , You gussed it Right...")
        print("You finished in",count,"Attempts")
        break

if n == sec_num:
    None
else:
    print("Game Over!, You are Out of Attempts")
    print("Don't Worry, Try again!")