age = int(input("Enter the person's age: "))

if age < 0:
    print("Invalid age")
elif age <= 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age <= 64:
    print("The person is an adult.")
else:
    print("The person is a senior citizen.")