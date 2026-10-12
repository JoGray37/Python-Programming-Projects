# Question 7: Pennies for Pay

days = int(input("Enter the number of days:"))

pennies = 1
total = 0

print("Day\tSalary")

for day in range(1, days + 1):
    print(day, "\t$", format(pennies / 100, ".2f"))
    total += pennies
    pennies *= 2

print("Total pay: $", format(total / 100, ".2f"))