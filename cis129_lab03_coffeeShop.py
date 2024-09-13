# Prices
coffee_price = 5
muffin_price = 4
tax_rate = 0.06

# Header for the shop
print("***************************************")
print("My Coffee and Muffin Shop")

# User input
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))

# Calculate subtotal
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal = subtotal_coffee + subtotal_muffin

# Calculate tax
tax = subtotal * tax_rate

# Calculate total amount due
total = subtotal + tax

# Receipt header
print("***************************************")
print("My Coffee and Muffin Shop Receipt")

# Detailed receipt
if num_coffees > 0:
    print(f"{num_coffees} Coffee{'s' if num_coffees > 1 else ''} at ${coffee_price} each: ${subtotal_coffee:.2f}")
if num_muffins > 0:
    print(f"{num_muffins} Muffin{'s' if num_muffins > 1 else ''} at ${muffin_price} each: ${subtotal_muffin:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
