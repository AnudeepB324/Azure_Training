#Division Check of two numbers

First_Number = int(input("Enter the first number"))
Second_Number = int(input("Enter the Second number"))
if (First_Number%Second_Number) == 0:
    print(f"Given first number '{First_Number}' is divible by the second number '{Second_Number}'")
else:
    print(f"Given first number '{First_Number}' is not divible by the second number '{Second_Number}',and the Remainder is: {First_Number%Second_Number}")    