def calculate_property_tax(actual_value):
    assessment_value = actual_value * 0.60
    property_tax = assessment_value * 0.0072

    print(f"Assessment Value: ${assessment_value:,.2f}")
    print(f"Property Tax: ${property_tax:,.2f}")

actual_value = float(input("Enter the actual property value: $"))
calculate_property_tax(actual_value)