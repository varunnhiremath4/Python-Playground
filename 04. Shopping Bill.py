print("="*30)
print("      Creating your Shopping Bill")
print("="*30)

Name = input("Enter your Name: ")
print("."*30)
product1= input("Enter the name of product 1: ")
price1 = float(input("Enter the price of product 1: "))
print("."*30)

product2= input("Enter the name of product 2: ")
price2 = float(input("Enter the price of product 2: "))
print("."*30)

product3= input("Enter the name of product 3: ")
price3 = float(input("Enter the price of product 3: "))
print("."*30)

product4= input("Enter the name of product 4: ")
price4 = float(input("Enter the price of product 4: "))
print("."*30)

product5= input("Enter the name of product 5: ")
price5 = float(input("Enter the price of product 5: "))

total_price = price1 + price2 + price3 + price4 + price5

print("-"*30)

discount = total_price * 0.10
Gift_Card = "Congratulations! You have received a gift card of Rs. 100 Also"
Final_price = total_price - discount

print("="*30)
print("      SHOPPING BILL")
print("="*30)

print("Customer Name: ", Name)
print("Your products are in the below list")
print([product1, product2, product3, product4, product5])
print("-"*30)
print("Total Price: ", total_price)
if total_price >= 2000:
    print("Discount: ",discount)
    print(Gift_Card)
elif total_price >= 1000:
    print("Discount: ",discount)
else:
    print("No Discounts Available for you")

print("Final Price: ", Final_price)
print("="*30)
print("Thank you for shopping with us! Have a great day!")
print("="*30)