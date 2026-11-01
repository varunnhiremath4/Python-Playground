inventory = [
    ("Noodles", 10, 30),
    ("Chips", 20, 50),
    ("Chocolates", 5, 20),
    ("Milk", 28, 10),
    ("Aloo Bujiya", 200, 5),
]

total_inventory = 0
highest = inventory[0][1]
lowest = inventory[0][1]
highest_name = inventory[0][0]
lowest_name = inventory[0][0]
low_quan = inventory[0][2]
low_quaname = inventory[0][0]

for i in inventory:
    Product_Name, Price, Quantity = i
    print("Product:", Product_Name, " Price:", Price, " Quantity:", Quantity)
    print("Total Value of", Product_Name, "is: ", Price*Quantity)
    print("-"*30)
    total_inventory += Price*Quantity

    if Price > highest:
        highest = Price
        highest_name = Product_Name
    elif Price < lowest:
        lowest = Price
        lowest_name = Product_Name

    if Quantity < 10:
        low_quan = Quantity
        low_quaname = Product_Name
        print("="* 30)
        print("Low Stock Alert for", low_quaname, "only", low_quan, "Left!")
        print("="* 30)
                          
print("Total Value of inventory: ", total_inventory)
print("The Expensive Item in Inventory is: ", highest_name, "->", highest)
print("The Cheapest item in Inventory is: ", lowest_name, "->", lowest)
print("="*30)

p_input = input("Enter the product you want to purchase: ")

found = False
for j in inventory:
    Product_Name, Price, Quantity = j
    
    if Product_Name == p_input:
        found = True
        print("Item Found!")
        q_input = int(input("How Much? "))
        newq = Quantity - q_input

        new_product = Product_Name, Price, newq
        inventory[inventory.index(j)] = new_product
        print("The Updated Inventory is: ")
        for k in inventory:
            print(k)

if found == False:
    print("Item not Found!")