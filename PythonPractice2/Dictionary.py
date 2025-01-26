# Adding the keys and values for the toppings
topping_names = {"Chocolate Chips" : 2.5 ,
                  "Whipped Cream" : 1.5 ,
                   "Gummy Bears" : 1,
                   "blueberry" : 4  }

# Selecting the toppings
selected_toppings = ("Chocolate Chips" ,"Whipped Cream" , "Gummy Bears" )

#Calculate the total cost if based on the customer selected three toppings
total_cost = sum (topping_names[toppings] for toppings in selected_toppings)
print(f"total cost for the selected groups is: {total_cost}")
