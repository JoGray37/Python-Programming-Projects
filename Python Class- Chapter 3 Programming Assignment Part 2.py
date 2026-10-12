quantity = int(input("Enter the number of packages purchases: "))

price = 120

if quantity < 0:
    print("Invalid quantity")
else:
    if quantity >= 31:
        discount_rate = 0.30
    elif quantity >= 21:
        discount_rate = 0.22
    elif quantity >=16:
        discount_rate = 0.15
    elif quantity >= 10:
        discount_rate = 0.10
    else:
        discount_rate = 0

    subtotal = quantity * price
    discount = subtotal * discount_rate
    total = subtotal - discount

    print(f"Discount Amount: ${discount:.2f}")
    print(f"Total Quantity: {quantity:.2f}")
    print(f"Total Purchase: ${total:.2f}")