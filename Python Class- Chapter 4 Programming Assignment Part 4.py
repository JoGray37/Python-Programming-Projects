# Question 8: Sum of Numbers

total = 0

number = float(input("Enter a positive number: "))

while number >= 0:
    total += number
    number = float(input("Enter a positive number (negative number to stop): "))

print("The sum is:", total)