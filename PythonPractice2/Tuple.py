# Adding the prices of the base icecreams
base_icecreams =  ((3.5, "Vanilla"),
(4.0, "Chocolate"),
(3.8, "Strawberry"),
(4.2, "Mint"),
(4.5, "Cookies and Cream")
)

#Using tuple for getting most and less expensive icreams
base_ice_creams_tuple = tuple(base_icecreams.items())
most_expensive = base_ice_creams_tuple[-1]
least_expensive = base_ice_creams_tuple[0]

print(f"the least expensive ice cream is : {least_expensive}")
print(f"the most expensive ice cream is : {most_expensive}")