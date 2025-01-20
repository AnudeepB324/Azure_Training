#Checking Grade based on the Marks Entered

Marks =int(input("Enter the Msrks for grading"))
if Marks >= 90 and Marks <= 100:
    Grade = "A"
elif Marks >= 80 and Marks <= 89:
    Grade = "B"
elif Marks >= 70 and Marks <= 79:
    Grade = "C"
elif Marks >= 60 and Marks <= 69:
    Grade = "D"
else:
    Grade = "F"
print(f"Student got a Grade of: {Grade}")

    