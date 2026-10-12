# Question 1: Multiplication Table

number = int(input("Enter the multiplication table you want to print: "))
print("Multiplication Table for", number)
for count in range(1, 11):
    product = number * count
    print(number, "x", count, "=", product)