ice_cream_prices = {
    'Scoop': 2.50,
    'Pre-Packaged': 5.00
}

order = {
    'Scoop': 1,            
    'Pre-Packaged': 2      
}

flavors = ['Vanilla', 'Chocolate', 'Strawberry']
toppings = ['Chocolate Chips', 'Whipped Cream', 'Sprinkles', 'Gummy Bears']

total_cost = 0

# For loop for generating all the combinations
print("Flavor and Topping Combinations:")
for flavor in flavors:
    for topping in toppings:
        print(f"{flavor} + {topping}")

# for printing Receipt
print("Customer Receipt:")
for item, quantity in order.items():
    price = ice_cream_prices[item] * quantity
    total_cost += price
    print(f"{quantity} x {item}: ${price:.2f}")

print(f"Total: ${total_cost:.2f}")