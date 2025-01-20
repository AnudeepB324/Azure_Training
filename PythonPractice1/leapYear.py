# checking Leap year or not 

Year=int(input("Please enter the year to check whether it is leap year or not"))
if Year%4==0 and Year%100!=0 or( Year%400==0):
        print("Entered year '{Year}' is a leap year")
else:
    print("Entered year '{Year}'  is not a leap year")