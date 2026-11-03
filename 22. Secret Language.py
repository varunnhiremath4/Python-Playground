lazy import random
lazy import string

print("="*35)
print("Secret Code Language Translator🔐")
print("="*35)
print("Select what you wanna do?")
print("1. Coding")
print("2. Decoding")
print("3. Exit Menu")
choice = int(input("Enter Your Choice from(1/2/3): "))
while choice!=3:
    if choice == 1:
        text_input = input("Type your word to be Encrypted: ")
        count = 0
        for i in text_input:
            count += 1
        if count < 3:
            print("Your Encrypted word is: ",text_input[::-1])
        else:
            random_letters1 = random.choices(string.ascii_letters,k=3)
            random_letters2 = random.choices(string.ascii_letters,k=3)
            print("-"*50)
            print("Your Encrypted word is: ","".join(random_letters1)+text_input[1:]+text_input[0]+"".join(random_letters2))
            print("Copy your Encrypted Word and use it")
            print("-"*50)
    elif choice == 2:
        word_input = input("Type the word to be Decrypted: ")
        count = 0
        for i in word_input:
            count += 1
        if count<3:
            print("Your Decrypted Word is: ", word_input[::-1])
        else:
            revoke_first = word_input[3:]
            revoke_second = revoke_first[:-3]
            final_word = revoke_second[-1]+revoke_second[0:-1]
            print("Your Decrypted Word is: ",final_word)
    else:
        print("Invalid Option!,please select again")
    choice2_input = input("Wanna try again[y/n]: ")
    if choice2_input.lower() == "y":
        print("Select what you wanna do?")
        print("1. Coding")
        print("2. Decoding")
        print("3. Exit Menu")
        choice = int(input("Enter Your Choice from(1/2/3): "))
    elif choice2_input.lower() == "n":
        print("Thanks for using me!")
        print("Program Closed")
        break
