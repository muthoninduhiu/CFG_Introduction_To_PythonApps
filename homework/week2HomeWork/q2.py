def calculate_vat(amount):
    total = amount * 1.2
    return total


result = calculate_vat(100)
print("The VAT is " + str(result) + "$")
