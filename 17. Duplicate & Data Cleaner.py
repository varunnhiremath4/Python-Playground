print("="*30)
print("   Duplicate & Data Cleaner")
print("="*30)

morning_data = [
    "Python", "Maths", "Physics", "Python",
    "Chemistry", "Maths", "English"
]

afternoon_data = [
    "Physics", "Python", "Biology", "Maths",
    "Biology", "Computer Science", "English"
]
print("Raw Morning data: ", morning_data)
print("Raw Afternoon data: ", afternoon_data)
print("-"*50)
morning_unique = set(morning_data)
afternoon_unique = set(afternoon_data)
print("-"*50)
print("The Unduplicated Morning Data is: ", morning_unique)
print("The Unduplicated Afternoon Data is: ", afternoon_unique)
print("-"*50)
common_subjects = morning_unique & afternoon_unique
print("The subjects which are common: ", common_subjects)
morning_only = morning_unique - afternoon_unique
print("-"*50)
print("the subjects only in morning: ", morning_only)
afternoon_only = afternoon_unique - morning_unique
print("The subjects only in afternoon: ", afternoon_only)
print("-"*50)
morning_seen = set()
morning_dupli = set()

for subject in morning_data:
    if subject not in morning_seen:
        morning_seen.add(subject)
    else:
        morning_dupli.add(subject)

print("The duplicate subjects in morning raw data: ", morning_dupli)

afternoon_seen = set()
afternoon_dupli = set()

for subject in afternoon_data:
    if subject not in afternoon_seen:
        afternoon_seen.add(subject)
    else:
        afternoon_dupli.add(subject)

print("The duplicate in afternoon raw data: ", afternoon_dupli)
print("-"*50)
all_unique_subjects = morning_unique | afternoon_unique
num_all_unique = len(all_unique_subjects)
print("Total unique subejcts from both morning and afternoon: ", all_unique_subjects)
print("Total Number of unique subjects from both morning and afternoon; ", num_all_unique)