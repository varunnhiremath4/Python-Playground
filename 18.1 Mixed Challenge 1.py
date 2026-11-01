print("="*30)
print("     Mixed Challenge 1")
print("="*30)
#the main given dictionary
students = {
    "Varun": ["Python", "Maths", "Physics"],
    "Ananya": ["Maths", "Chemistry"],
    "Mayank": ["Python", "Maths", "Computer Science"],
    "Rahul": ["Physics", "Chemistry"],
    "Karthik": ["Python", "Physics", "Maths"]
}

#This block is for displaying and counting all unique subjects 
all_unique_subjects = set()
for sub_list in students.values():
    for sub in sub_list:
        all_unique_subjects.add(sub)
print("-"*50)
print("The total unique subject are: ")
print(all_unique_subjects)
len_all_unique_sub = len(all_unique_subjects)
print("The total number of unique subjects are: ", len_all_unique_sub)

#This block is for displaying python students
python_students = []
for name, subjects in students.items():
    if "Python" in subjects:
        python_students.append(name)
print("-"*50)        
print("The Python studing students are: ")
print(python_students)

#This is to display the students who have taken python and maths both
python_maths_students = []
for name2, subjects2 in students.items():
    if "Python" in subjects2 and "Maths" in subjects2:
        python_maths_students.append(name2)
print("-"*50)        
print("The students who have taken Python and Maths both: ")
print(python_maths_students)
print("-"*50)

#This is the dict which is representing the students in list with respective subjects
subject_students = {}
for name, subjects in students.items():
    for sub in subjects:
        if sub not in subject_students:
            subject_students[sub] = [name]
        else:
            subject_students[sub].append(name)
            
print("The new Dictionary will be: ")
print(subject_students)