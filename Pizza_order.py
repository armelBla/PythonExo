print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L?").upper()
add_pepperoni = input("Do you want pepperoni? Y, N?").upper()
extra_cheese = input("Do you want extra cheese? Y, N?").upper()

if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price =20
elif size == "L":
    pizza_price = 25
else:
    print("Size not available")
    pizza_price = 0
# add pepperoni option
if add_pepperoni == "Y" and (size == "M" or size == "L"):
    total_price = pizza_price + 3
elif add_pepperoni == "Y" and size == "S":
    total_price = pizza_price + 3
else:
    total_price = pizza_price
# add cheese option
if extra_cheese == "Y":
    total_price += 1

print(f"Your final bill is: ${total_price}")
