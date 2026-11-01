expenses = [
    ("Food", 250),
    ("Travel", 120),
    ("Food", 180),
    ("Shopping", 500),
    ("Travel", 80),
    ("Entertainment", 300),
    ("Food", 150),
    ("Shopping", 250)
]

total_amount = 0
high_amt = expenses[0][1]
low_amt = expenses[0][1]
high_cat = expenses[0][0]
low_cat =expenses[0][0]

for i in expenses:
    category, amount = i
    print("Category:", category, " -> Amount Spent:", amount)
    total_amount += amount

    if amount>high_amt:
        high_amt = amount
        high_cat = category
    elif amount<low_amt:
        low_amt = amount
        low_cat = category

print("-"*30)
print("Total Money spent: ", total_amount)
print("The Highest spend is: ", high_cat, " ->", high_amt)
print("The Lowest spend is: ", low_cat, " ->", low_amt)
print("-"*30)

cat_input = input("The category for which you want to know the total amount spent? ")
total = 0
found = False
count_found = 0
for j in expenses:
    category, amount = j
    if cat_input == category:
        found = True
        count_found += 1
        print(cat_input, "Found", count_found, "time!") 
        total += amount
       
print("The total amount spent on", cat_input, "is", total)

if found is False:
    print("Category Not Found")
print("-"*30)

new_cat = input("Enter the Category you want to add to ypur expenses: ")
new_amt = int(input("Enter the amount you spent on that category: "))
print("Updation done in the Expenses, just check out!")
new_expenses = (new_cat, new_amt)
expenses.append(new_expenses)
new_total = 0
for k in expenses:
    category, amount = k
    new_total += amount
    print("Category:", category, " -> Amount Spent:", amount)
print("-"*30)
print("The total after updating is: ", new_total)
print("="*30)  