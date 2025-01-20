
# Positive or Negative

number = int(input("Enter a number to check whether it is Positive, Negative, or Zero: "))
if (number%2 == 0 and number!=0):
    print(f"Entered value '{number}' is a Positive number!")   
elif (number%2==1):
    print(f"Entered value '{number}' is a Negative number!")
else:
    print(f"Entered value is a Zero!")