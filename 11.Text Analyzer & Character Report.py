print("="*30)
print("         Text Analysis")
print("="*30)
text = input("Enter your Text: ")
total_counter = 0
Alphabet_counter = 0
Digit_counter = 0
Space_counter = 0
Upper_counter = 0
Lower_counter = 0
Vowel_counter = 0
Consonant_counter = 0
Vowels = ("A", "a", "U", "u", "E", "e", "I", "i", "o", "O")


for m in text:
    total_counter += 1

    if m.isalpha():
        Alphabet_counter += 1
        if m in Vowels:
            Vowel_counter += 1
        else:
            Consonant_counter += 1
    if m.isdigit():
        Digit_counter += 1
    if m == " ":
        Space_counter += 1
    if m.isupper():
        Upper_counter += 1
    if m.islower():
        Lower_counter += 1

print("Total number of Characters: ", total_counter)
print("Total number of Alphabets: ", Alphabet_counter)
print("Total Number of Spaces: ", Space_counter)
print("Total number of Digits: ", Digit_counter)
print("Total number of Uppercase: ", Upper_counter)
print("Total number of Lowercase: ", Lower_counter)
print("Total number of Vowels: ", Vowel_counter)
print("Total number of Consonants: ", Consonant_counter)
print("="*30)
print("      Character reports")
print("="*30)

for n in text:
    if n in Vowels:
        if n.isupper():
            print(n," -> Vowel -> UpperCase")
        elif n.islower():
            print(n," -> Vowel -> LowerCase")
        else:
            None
            
    elif n == " ":
        print(n," -> Space")

    else:
        if n.isupper():
            print(n," -> Consonant or Other -> UpperCase")
        elif n.islower():
            print(n," -> Consonant or Other -> LowerCase")
        else:
            None