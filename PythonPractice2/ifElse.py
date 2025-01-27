classics = ['VANILLA', 'CHOCOLATE', 'STRAWBERRY']
trendy_flavors = ['SALTED CARAMEL', 'MATCHA', 'COOKIES & CREAM']
kid_friendly = ['RAINBOW SHERBET', 'BUBBLEGUM', 'COTTON CANDY']

suggested_cities = ['NEW YORK', 'LOS ANGELES', 'CHICAGO', 'HOUSTON', 'PHOENIX', 'SAN DIEGO', 'DALLAS']

city = input("Enter the city name: ").upper()

# If condition to determine the city is in the list
if city in suggested_cities:
    print("Valid city")
else:
    print("Invalid city")

flavor = input("Enter the ice cream flavor: ").upper()

# If condition to determine the flavour Classification
if flavor in classics:
    print(f"{flavor} is a Classic flavor.")
elif flavor in trendy_flavors:
    print(f"{flavor} is a Trendy flavor.")
elif flavor in kid_friendly:
    print(f"{flavor} is a Kid-Friendly flavor.")
else:
    print(f"Sorry, {flavor} is not in our flavor list.")